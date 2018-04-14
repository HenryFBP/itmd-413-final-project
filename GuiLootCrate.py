from LootCrate import *


class GuiLootCrate:
    """
    A class that exists to turn a LootCrate into a tkinter GUI element.
    """

    @staticmethod
    def crate_to_frame(crate: LootCrate, parent):
        """
        :return: ``crate`` as a ``tkinter`` ``Frame`` object.
        """
        rf = Frame(parent, bd=2, relief=SUNKEN)

        name = Label(rf, text=crate.name)

        items = GuiLootCrate.crate_items_to_frame(crate, rf)

        items.pack()

        name.pack()

        return rf

    @staticmethod
    def crate_items_to_frame(crate: LootCrate, parent):
        rf = Frame(parent)

        print("crate items to frame")

        for item in crate.pool:
            item: LootItem
            itemf = Frame(rf, bd=2, relief=SUNKEN)

            iteml = Label(itemf, text=item.name)
            iteml.pack()
            itemf.pack()

        print("end of crate_items_to_frame")
        return rf
