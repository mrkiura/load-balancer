from flask import Flask
import random
import requests
from config import config
from flask import Flask, request


loadbalancer = Flask(__name__)

TURURU_BACKENDS = ['localhost:8081', 'localhost:8082']
WAWAWA_BACKENDS = ['localhost:9081', 'localhost:9082']



@loadbalancer.route('/')
def router():
    host_header = request.headers.get('Host')
    for entry in config['hosts']:
        if host_header == entry['host']:
            backend = random.choice(entry["servers"])
            response = requests.get(f'http://{backend}')
            return response.content, response.status_code

    else:
        return 'Not Found. tururu', 404


@loadbalancer.route('/tururu')
def tururu():
    backend = random.choice(TURURU_BACKENDS)
    response = requests.get(f'http://{backend}')
    return response.content, response.status_code


@loadbalancer.route('/wawawa')
def wawawa():
    backend = random.choice(WAWAWA_BACKENDS)
    response = requests.get(f'http://{backend}')
    return response.content, response.status_code
