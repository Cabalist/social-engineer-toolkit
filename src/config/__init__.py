# coding=utf-8
import os

import validate
from configobj import ConfigObj

cfg_spec = """
accepted_license = boolean(default=False)
SET_dir = string(default='.set')
AIRBASE_NG_PATH = string(default='/usr/local/sbin/airbase-ng')
DNSSPOOF_PATH=string(default='/usr/local/sbin/dnsspoof')


# canvas_border = integer(min=10, max=35, default=15)
# colour1 = list(min=3, max=3, default=list('280', '0', '0'))
# colour2 = list(min=3, max=3, default=list('255', '255', '0'))
# colour3 = list(min=3, max=3, default=list('0', '255', '0'))
# colour4 = list(min=3, max=3, default=list('255', '0', '0'))
# colour5 = list(min=3, max=3, default=list('0', '0', '255'))
# colour6 = list(min=3, max=3, default=list('160', '32', '240'))
# colour7 = list(min=3, max=3, default=list('0', '255', '255'))
# colour8 = list(min=3, max=3, default=list('255', '165', '0'))
# colour9 = list(min=3, max=3, default=list('211', '211', '211'))
# convert_quality = option('highest', 'high', 'normal', default='normal')
# default_font = string
# default_width = integer(min=1, max=12000, default=640)
# default_height = integer(min=1, max=12000, default=480)
# imagemagick_path = string
# handle_size = integer(min=3, max=15, default=6)
# language = option('English', 'English (United Kingdom)', 'Russian', 'Hindi', default='English')
# print_title = boolean(default=True)
# statusbar = boolean(default=True)
# toolbar = boolean(default=True)
# toolbox = option('icon', 'text', default='icon')
# undo_sheets = integer(min=5, max=50, default=10)
"""


def create_config(path):
    """
    Create a config file using a configspec
    and validate it against a Validator object
    """
    spec = cfg_spec.split("\n")
    config = ConfigObj(path, configspec=spec)
    config["SET_dir"] = os.path.join(os.path.expanduser("~"), ".set")

    validator = validate.Validator()
    config.validate(validator, copy=True)
    config.filename = path
    config.write()


def get_config(path=os.path.join(os.path.expanduser("~/.set/config.ini"))):
    new_config = ConfigObj(os.path.join(path), configspec=cfg_spec.split("\n"))
    validator = validate.Validator()
    new_config.validate(validator, copy=True)
    return new_config

CONFIG = get_config()

