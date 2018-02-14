import sys
import pygtk


class LootCrateGUI:
    def on_window1_destroy(self, object, data=None):
        print("quit with cancel")
        gi.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print("quit from menu")
        Gtk.main_quit()

    def __init__(self):
        self.gladefile = "gui_GLADE.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("windowRoot")
        self.window.show()


if __name__ == "__main__":
    main = LootCrateGUI()
    Gtk.main()
