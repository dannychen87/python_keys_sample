from common.yaml_utils import read_yaml


class ConfigFactory:

    def __init__(self):
        self.config = read_yaml('./common/config.yaml')

    def fetch(self, key):
        return self.config[key]

    def base_url(self):
        return self.fetch('endpoint')

    def browser(self):
        return self.fetch('browser')

    def timeout(self):
        return self.fetch('timeout')
