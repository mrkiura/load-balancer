import requests


class Server:
    def __init__(self, endpoint: str, path:str="/healthcheck"):
        self.endpoint = endpoint
        self.path = path
        self.healthy = True
        self.scheme = "http://"
        self.timeout = 1

    def healthcheck_and_update_status(self):
        try:
            response = requests.get(self.scheme + self.endpoint + self.path, timeout=self.timeout)
            if response.ok:
                self.healthy = True
            else:
                self.healthy = False
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            self.healthy = False

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Server):
            return self.endpoint == other.endpoint
        return False

    def __repr__(self) -> str:
        return f'<Server: {self.endpoint} {self.healthy} {self.timeout}>'