import os
import yaml
import logging
import json
from types import SimpleNamespace


def load_config():
    config_path = "/Users/najmuzsakib/Documents/Projects/PythonProjects/AuthServerTestSecrets/config.yaml"
    config_env_path = os.environ.get('config', config_path)
    return yaml.load(open(config_env_path, 'r'), Loader=yaml.FullLoader)

def get_default_logger(name):
    log_file_path = '/var/log/QuranApi/quran.log'
    log_format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'

    # logging.basicConfig(filename='quran.log', format= log_format, level=logging.DEBUG)

    # Gets or creates a logger
    logger = logging.getLogger(name)

    # set log level
    logger.setLevel(logging.DEBUG)
    # ... (other imports and code)



    # ... added code--------------

    log_directory = '/var/log/QuranApi'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    file_handler = logging.FileHandler(os.path.join(log_directory, 'quran.log'))

    # ... (rest of the code)

    # define file handler and set formatter
    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

def dict_to_object(dict):
    info_json = json.dumps(dict)
    info_obj = json.loads(info_json, object_hook=lambda d: SimpleNamespace(**d))
    return info_obj

def read_file(path):
    f = open(path)
    content = f.read()
    return content


