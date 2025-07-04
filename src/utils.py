import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_class_names(config_path):
    import yaml
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['names']
