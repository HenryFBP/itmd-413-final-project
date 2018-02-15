from tkinter import *

from guiLib import *


class GuiLootItem:
    """
    A class that exists to turn a LootItem into a tkinter GUI element.
    """

    def item_to_frame(item: LootItem, parent) -> Frame:
        """
        :return: ``item`` as a tkinter Frame object.
        """

        frame = Frame(parent, bd=2, relief=SUNKEN, background=("#" + random_hex_string()))

        label = Label(frame, text=item.name)
        label.pack()

        return frame
