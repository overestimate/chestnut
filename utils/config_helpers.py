import appdirs
import os

config_dir = appdirs.user_data_dir('Chestnut', 'overestimate')
if 'CN_CONF_PATH' in os.environ:
    config_dir = os.environ['CN_CONF_PATH']


def create_config_dir():
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)

def is_first_run():
    return not os.path.exists(
        os.path.join(config_dir, 'has_finished_fts')
    )

def debug_file_present():
    return os.path.exists(
        os.path.join(config_dir, 'debug_enabled')
    )

def set_has_run(): 
    open(
        os.path.join(config_dir, 'has_finished_fts'),
        'w').close() # don't care about contents.