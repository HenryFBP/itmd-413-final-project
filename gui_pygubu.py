from pygubu import *

from GuiLootItem import *


def parent(w: Widget):
    """
    :param w: The child widget.
    :return: The parent of widget ``w``.
    """
    return w.nametowidget(name=w.winfo_parent())


class Application:
    def on_horizontal_scroll(self: Scrollbar, event: Event):
        print("Horiz scroll?")
        x = self.get()

    def on_quit_button_click(self: Tk):
        self.mainwindow.quit()

    def on_play_button_click(self: Tk):
        itemFrame = GuiLootItem.item_to_frame(randomLootItem(), self.inventory)

        itemFrameRow = (len(self.inventory.children) if isinstance(len(self.inventory.children), int) else 0)

        itemFrame.grid(row=itemFrameRow, sticky=NSEW)

    def __init__(self, master, path="./gui_pygubu.ui"):
        # make list of functions inside ``Application`` class.
        methods = [func for func in dir(Application) if (  # for ALL props of Application class, and add them IF
            callable(getattr(Application, func)) and  # if it is callable
            func.startswith("on_")  # if it starts with ``on_``.
        )]

        print("Methods:")
        print(repr(methods) + "\n")

        # configure callbacks
        callbacks = {}

        # this is easier than doing:
        # callbacks = {"on_thing" : on_thing_function,
        #              "on_ding" : on_ding_function ...}
        for func in methods:
            callbacks[func] = getattr(self, func)

        print("Callbacks:")
        print(repr(callbacks).replace(',',',\n') + "\n")

        # 1: Create a builder
        self.builder = Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)

        # Get inventory pane to add stuff to
        self.inventory: Frame = self.builder.get_object('Frame_inventory', master)

        # get scrollbar to register horizontal scroll event
        self.inventoryScroll: Scrollbar = parent(self.inventory)

        # self.inventoryScroll.bin

        # connect method callbacks
        unconnected = self.builder.connect_callbacks(callbacks)

        print("Unconnected callbacks:")
        print(repr(unconnected) + "\n")


if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # don't show blank window

    app = Application(root)
    root.mainloop()
