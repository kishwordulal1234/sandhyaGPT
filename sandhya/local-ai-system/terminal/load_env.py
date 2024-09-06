import os
import yaml
import json

def load_yaml_env(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def load_json_env(path):
    with open(path, 'r') as file:
        return json.load(file)

def load_env():
    yaml_path = os.path.join('env', 'yaml', 'settings.yaml')
    json_path = os.path.join('env', 'json', 'settings.json')

    env = {}
    if os.path.exists(yaml_path):
        env.update(load_yaml_env(yaml_path))
    if os.path.exists(json_path):
        env.update(load_json_env(json_path))

    for key, value in env.items():
        os.environ.setdefault(key, value)
