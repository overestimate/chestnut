import utils.log as log

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk
import traceback

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.set_default_size(600,480)
        self.set_name('Chestnut')
        self.set_title('Chestnut')
        
        self.some_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.some_box)

        self.some_button = Gtk.Button(label='test logging funcs')
        self.some_box.append(self.some_button)
        self.some_button.connect('clicked', self.meow)

    def meow(self, button: Gtk.Button):
        log.debug('this is a debug message')
        log.warn('this is a warning')
        log.error('this is an error')
        log.info('this is an info message')