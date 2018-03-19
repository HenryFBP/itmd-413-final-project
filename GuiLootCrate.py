from LootCrate import *


class GuiLootCrate:
    """
    A class that exists to turn a LootCrate into a tkinter GUI element.
    """

    def crate_to_frame(crate: LootCrate, parent):
        """
        :return: ``crate`` as a ``tkinter`` ``Frame`` object.
        """
        rf = Frame(parent, bd=2, relief=SUNKEN)

        name = Label(rf, text=crate.name+"OMG LOOK")

        name.pack()

        return rf
