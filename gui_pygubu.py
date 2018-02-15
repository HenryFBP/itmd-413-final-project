import pygubu

from GuiLootItem import *


class Application:
    def on_quit_button_click(self):
        self.mainwindow.quit()

    def on_play_button_click(self):
        itemFrame = GuiLootItem.item_to_frame(randomLootItem(), self.inventory)

        itemFrameRow = (len(self.inventory.children) if isinstance(len(self.inventory.children), int) else 0)

        itemFrame.grid(row=itemFrameRow, sticky=NSEW)

        itemFrame.pack()

        self.inventory.add(itemFrame)

    def __init__(self, master, path="./gui_pygubu.ui"):
        # make list of functions inside ``Application`` class.
        methods = [func for func in dir(Application) if (  # for ALL props of Application class, and add them IF
            callable(getattr(Application, func)) and  # if it is callable
            func.startswith("on_")  # if it starts with ``on_``.
        )]

        # print("Methods:")
        # print(methods)

        # configure callbacks
        callbacks = {}

        for func in methods:
            callbacks[func] = getattr(self, func)

        # print("Callbacks:")
        # print(callbacks)

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
