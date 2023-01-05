import appdirs
import os

config_dir = appdirs.user_data_dir('Chestnut', 'overestimate')
if 'CN_CONF_PATH' in os.environ:
    config_dir = os.environ['CN_CONF_PATH']

def debug_file_present():
    return os.path.exists(
        os.path.join(config_dir, 'debug_enabled')
    )

if debug_file_present():
    os.remove(os.path.join(config_dir, 'debug_enabled'))
    print('debug is OFF')
else:
    open(
        os.path.join(config_dir, 'debug_enabled'),
        'w').close()
    print('debug is ON')