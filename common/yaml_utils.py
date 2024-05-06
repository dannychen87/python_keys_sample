import yaml


def read_yaml(path):
    with open(path, encoding='utf-8') as f:
        return yaml.load(stream=f, Loader=yaml.FullLoader)


def clean_yaml(path):
    with open(path, encoding='utf-8', mode='w') as f:
        f.truncate()


def save_to_yaml(path, values):
    with open(path, encoding='utf-8', mode='a') as f:
        yaml.dump(values, stream=f, allow_unicode=True)
