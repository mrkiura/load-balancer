import yaml

from models import Server
from utils import transform_backends_from_config


def test_transform_backends_from_config():
    input_config = yaml.safe_load("""
        hosts:
          - host: www.mango.com
            servers:
              - localhost:8081
              - localhost:8082
          - host: www.apple.com
            servers:
              - localhost:9081
              - localhost:9082
        paths:
          - path: /mango
            servers:
              - localhost:8081
              - localhost:8082
          - path: /apple
            servers:
              - localhost:9081
              - localhost:9082
    """
    )
    output = transform_backends_from_config(input_config)
    assert list(output.keys()) == ['www.mango.com', 'www.apple.com', '/mango', '/apple']
    assert output['www.mango.com'][0] == Server('localhost:8081')
    assert output['www.mango.com'][1] == Server('localhost:8082')
    assert output['www.apple.com'][0] == Server('localhost:9081')
    assert output['www.apple.com'][1] == Server('localhost:9082')
    assert output['/mango'][0] == Server('localhost:8081')
    assert output['/mango'][1] == Server('localhost:8082')
    assert output['/apple'][0] == Server('localhost:9081')
    assert output['/apple'][1] == Server('localhost:9082')