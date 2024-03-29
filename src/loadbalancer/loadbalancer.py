from flask import Flask
import random
import requests
from flask import Flask, request

from loadbalancer.utils import (
    get_healthy_server,
    healthcheck,
    transform_backends_from_config,
    process_header_rules
)
from loadbalancer.config import config

balancer = Flask(__name__)

register = transform_backends_from_config(config)


@balancer.route('/')
def router():
    """Route requests to the correct backend server based on the host.
    """
    updated_register = healthcheck(register)
    host_header = request.headers.get('Host')
    for entry in config['hosts']:
        if host_header == entry['host']:
            healthy_server = get_healthy_server(entry["host"], updated_register)
            if not healthy_server:
                return 'No backend servers available.', 503
            headers = process_header_rules(config, host_header, {k: v for k, v in request.headers.items()})
            response = requests.get(f'http://{healthy_server.endpoint}', headers=headers)
            return response.content, response.status_code

    return 'Not Found.', 404


@balancer.route("/<path>")
def path_router(path):
    """Route requests to the correct backend server based on the path."""
    updated_register = healthcheck(register)
    for entry in config["paths"]:
        if f"/{path}" == entry["path"]:
            healthy_server = get_healthy_server(entry["path"], updated_register)
            if not healthy_server:
                return 'No backend servers available.', 503
            headers = process_header_rules(config, host_header, {k: v for k, v in request.headers.items()})
            response = requests.get(f'http://{healthy_server.endpoint}', headers=headers)
            return response.content, response.status_code
    return 'Not Found.', 404
