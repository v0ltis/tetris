import yaml
import os
import sys

def load() -> dict:
    """
    Load the config file
    
    Returns:
        dict: The config file
    """
    # obtain the absolute path of the config file
    file_path = os.path.dirname(sys.argv[0]) + "/config.yml"

    with open(file_path, 'r', encoding='UTF-8') as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.Loader)
