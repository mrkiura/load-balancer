import yaml
import random
from typing import TypedDict, Dict, Sequence
from config import Config

from models import Server


def load_config(path: str):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

def get_healthy_server(host, register) -> Server | None:
    try:
        server = random.choice([server for server in register[host] if server.is_healthy])
        return server
    except IndexError:
        return None

def transform_backends_from_config(config: Config) -> Dict[str, Sequence[Server]]:
    register = {}
    for entry in config.get("hosts", []):
        register.update({entry["host"]: [Server(endpoint) for endpoint in entry["servers"]]})
    for entry in config.get("paths", []):
        register.update({entry["path"]: [Server(endpoint) for endpoint in entry["servers"]]})
    return register
