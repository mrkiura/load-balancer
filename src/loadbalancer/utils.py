import yaml
import random
from typing import TypedDict, Dict, Sequence
from loadbalancer.config import Config

from loadbalancer.models import Server


def load_config(path: str) -> Config:
    """Load config from a yaml file."""
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config


def transform_backends_from_config(config: Config) -> Dict[str, Sequence[Server]]:
    """Transform the config into a register of servers."""
    register = {}
    for entry in config.get("hosts", []):
        register.update({entry["host"]: [Server(endpoint) for endpoint in entry["servers"]]})
    for entry in config.get("paths", []):
        register.update({entry["path"]: [Server(endpoint) for endpoint in entry["servers"]]})
    return register


def get_healthy_server(host: str, register) -> Server | None:
    """Get a healthy server from a list of healthy servers."""
    try:
        server = random.choice([server for server in register[host] if server.is_healthy])
        return server
    except IndexError:
        return None


def healthcheck(register: Dict[str, Sequence[Server]]):
    """Healthcheck all servers in the register.
    """
    for host in register:
        for server in register[host]:
            server.healthcheck_and_update_status()
    return register


def process_header_rules(config, host, rules):
    for entry in config.get("hosts", []):
        if host == entry.get("host"):
            header_rules = entry.get("header_rules", {})
            for instruction, header in header_rules.items():
                match instruction:
                    case "add":
                        rules.update(header)
                    case "remove":
                        for header_name in header.keys():
                            if header_name in rules:
                                del rules[header_name]
    return rules
