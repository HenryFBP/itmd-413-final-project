import pygubu

from GuiLootItem import *


class Application:
    def on_quit_button_click(self):
        self.mainwindow.quit()

    def on_play_button_click(self):
        itemFrame = GuiLootItem.item_to_frame(randomLootItem(), self.inventory)

        itemFrame.pack()

        self.inventory.add(itemFrame)

    def __init__(self, master, path="./gui_pygubu.ui"):
        # configure callbacks
        callbacks = {
            'on_quit_button_click': self.on_quit_button_click,
            'on_play_button_click': self.on_play_button_click,
        }

        # 1: Create a builder
        self.builder = pygubu.Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)

        # Get inventory pane to add stuff to
        self.inventory: PanedWindow = self.builder.get_object('Panedwindow_inventoryList', master)

        # connect method callbacks
        self.builder.connect_callbacks(callbacks)


if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # don't show blank window

    app = Application(root)
    root.mainloop()
