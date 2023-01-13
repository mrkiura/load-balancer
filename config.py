import yaml


def load_config(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config


config = load_config('loadbalancer.yaml')