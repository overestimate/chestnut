import utils.log as log
import sys
from . import main_window, first_time_setup, clicker_test

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk

class DevelWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_ref = kwargs['application'] # probably useless, lol.
        
        self.set_default_size(600,480) 
        self.set_name('Chestnut')
        self.set_title('Chestnut') # consistency? i hardly know her
        
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
        
        # this is stupid! oh well. if it does blow up, it probably will only affect me, as 
        # this will likely never see the light of day due to my lack of finishing things.

        window_list = [ main_window.MainWindow, first_time_setup.FirstTimeSetupWindow, clicker_test.ClickerTestWindow ]

        for window in window_list: # i hate this, but it will hopefully make development a *little* quicker? maybe?
            newButton = Gtk.Button(label=f'Open {window.__name__}')
            newButton.connect('clicked', 
                self.spawn_callback,
                window
            )
            self.main_box.append(newButton)
    def spawn_callback(self, button, window):
        if self.app_ref == None:
            log.error('app ref is none!')
            return
        self.current_window = window(application=self.app_ref)
        self.current_window.show()