import yaml
import os
from typing import TypedDict, List, Sequence



class HostServers(TypedDict):
    host: str
    servers: Sequence[str]

class PathServers(TypedDict):
    path: str
    servers: Sequence[str]

class Config(TypedDict):
    hosts: Sequence[HostServers]
    paths: Sequence[PathServers]


def load_config(path: str) -> Config:
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

filename = './src/loadbalancer/loadbalancer.yaml'
config = load_config(os.path.abspath(filename))