'''
Chestnut Launcher, (c) overestimate 2022-
Licensed under the MIT license. tl;dr: Do what you want, I'm not responsible.

This code has some useful flag parsing code. It has one feature I don't want to implement but want to have:
 - stacking flags with a value at the end.
     If i were to run `some_command -vvc 4`, I'd ideally want it to be the same as `some_command -v -v -c 4`.

'''

# basic sanity check to make sure we're running from main thread.
if __name__ != '__main__':
    exit()

import utils.config_helpers as config_helpers
from ui.windows.first_time_setup import FirstTimeSetupWindow
from ui.windows.main_window import MainWindow
from ui.windows.development import DevelWindow
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import os
import sys
from utils import log
import utils.config_helpers as config_helpers

# define shorthands and the long key equivalent.
shorthands = {
    '-w': '--window',
    '-v': '--verbose'
}

# define flags without values. use both if shorthands present.
no_value_flags = [ '-v' ]

# add long flags
for k,v in shorthands:
    if k in no_value_flags:
        if v not in no_value_flags: no_value_flags.append(v)

flags = []

# get all defined flags.
parsed_flags_raw = [(x, i) for i, x in enumerate(sys.argv) if x.startswith('-')]

# get shorthand stacks done now. causes us pain if we don't.
for i, t in enumerate(parsed_flags_raw.copy()):
    for k, v in shorthands:
        if t[0].startswith(k):
            f = t[0][1:]
            if len(f) == 1: break
            if f[0] != f[1]: break
            for c in f: flags += [('-' + c, None)]
            parsed_flags_raw.remove(t)
            break

# parse flags defined in `--flag=value` syntax
flags += [(x.split('=')[0], '='.join(x.split('=')[1:])) for x, _ in parsed_flags_raw if '=' in x]

# parse flags defined in `--flag value` syntax. much more tedious
for x, i in parsed_flags_raw:
    if '=' in x: continue
    if x in no_value_flags:
        flags += [(x, None)]
        continue
    flags += [(x, sys.argv[i+1])]

# convert shorthand flags to long ones, leaving shorthands for now
for x,y in shorthands.items():
    for k,v in flags:
        if k == x:
            flags += [(y,v)]


# remove shorthands
flags_copy = flags.copy() # so we can operate on the original set
for i, x in enumerate(flags_copy):
    if shorthands.get(x[0]) is not None:
        flags.remove(x)

# set up flags_present
flags_present = []
for k, _ in flags:
    if k not in flags_present: flags_present.append(k)

# create final flags list, making lists of values.
final = {}
for k, v in flags:
    if k in final.keys():
        if isinstance(final.get(k), list): final.update({k: final.get(k) + [v]})
        else: final.update({k:[final.get(k), v]})
    else:
        final.update({k:v})

# convert None lists to numbers
for k, v in final.items():
    if type(v) != list: continue
    if False not in [x == None for x in v]:
        final[k] = len(v)



window_param = final.get('--window')
window = MainWindow

if window_param == 'devel':
    window = DevelWindow
elif window_param == 'fts':
    window = FirstTimeSetupWindow

class Chestnut(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    # this should be it's own thing!
    def on_activate(self, app):
        global window # stupid
        config_helpers.create_config_dir()

        # hard overrides. these take priority over cmd-line.
        if config_helpers.debug_file_present() or 'CN_DEBUG' in os.environ:
            window = DevelWindow
        elif config_helpers.is_first_run() or 'CN_FORCE_FTS' in os.environ:
            window = FirstTimeSetupWindow
            config_helpers.set_has_run()

        self.win = window(application=app)
        self.win.present()


app = Chestnut(application_id='net.overestimate.Chestnut')
app.run()