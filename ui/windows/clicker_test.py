from utils import log

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk

@Gtk.Template(filename="ui/builder_files/clickertest.ui")
class ClickerTestWindow(Gtk.Window):
    _click_count = 0
    __gtype_name__ = "clickertest"
    clicker_label = Gtk.Template.Child()
    @Gtk.Template.Callback()
    def a_callback(self, button):
        self._click_count += 1
        pressString = f"You clicked {self._click_count} time{'s' if self._click_count != 1 else ''}."
        self.clicker_label.set_label(pressString)
