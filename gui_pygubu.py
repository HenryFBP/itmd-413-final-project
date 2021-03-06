from GuiLootCrate import *
from GuiLootCrateGraph import *


class MainGUI:
    def __init__(self, master, path="./gui_pygubu.ui"):
        # make list of functions inside ``Application`` class.
        methods = [func for func in dir(MainGUI) if (  # for ALL props of Application class, and add them IF
            callable(getattr(MainGUI, func)) and  # if it is callable
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
        print(repr(callbacks).replace(',', ',\n') + "\n")

        # 1: Create a builder
        self.builder = Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)

        # Get inventory pane to add stuff to
        self.inventory: Frame = self.builder.get_object('Frame_inventory', master)

        self.Frame_crate: Frame = self.builder.get_object('crate_open', master)

        # get crate frame display
        self.Frame_crate_display: Frame = self.builder.get_object('crate_open_display', master)

        # get scrollbar to register horizontal scroll event
        self.inventoryScroll: Scrollbar = parent(self.inventory)

        # how many kreds user wants to buy
        self.Entry_kreds: Entry = self.builder.get_object("Entry_kreds", master)

        # user's current kreds
        self.Label_balance: Label = self.builder.get_object('Label_balance', master)

        # how much will entered kreds cost?
        self.Label_kreds_to_money = self.builder.get_object('Label_kreds_to_money', master)

        # connect method callbacks
        unconnected = self.builder.connect_callbacks(callbacks)

        print("Unconnected callbacks:")
        print(repr(unconnected) + "\n")

        # load all our game's JSON info
        game = Game()

        self.game = game

        game.import_rarities("_data/loot_rarities.json")
        print("Rarities:")
        pprint(game.rarities)

        game.import_items("_data/loot_items.json")
        print("Items:")
        pprint(game.itempool)

        game.import_groups("_data/loot_groups.json")
        print("Groups:")
        pprint(game.itemgroups)

        game.import_crates("_data/loot_crates.json")
        print("Crates:")
        pprint(game.itemcrates)

        # update kreds view
        self.update_balance_view()

    def set_crate_frame(self, crate: LootCrate):
        """
        Puts ``crate``, a ``LootCrate``, inside of the loot crate display frame, wherever that is.

        Destroys all children inside of the Frame_crate_display. THERE CAN ONLY BE ONE!
        """
        for child in self.Frame_crate_display.winfo_children():
            child.destroy()

        cf = GuiLootCrate.crate_to_frame(crate, self.Frame_crate_display)

        cf.grid(row=0, sticky=NSEW)

    def on_horizontal_scroll(self: Scrollbar, event: Event):
        print("Horiz scroll?")
        x = self.get()

    def on_quit_button_click(self: Tk):
        self.mainwindow.quit()

    def on_left_crate_button_click(self: Tk):
        a = self.game.cycleLeft()
        self.set_crate_frame(a)

    def on_right_crate_button_click(self: Tk):
        b = self.game.cycleRight()
        self.set_crate_frame(b)

    def on_play_button_click(self: Tk):
        randomItem: LootItem = randomLootItem()

        itemFrame = GuiLootItem.item_to_frame(randomItem, self.inventory)

        itemFrameRow = (len(self.inventory.children) if isinstance(len(self.inventory.children), int) else 0)

        itemFrame.grid(row=itemFrameRow, sticky=NSEW)

    def update_balance_view(self: Tk, elt: Label = None):
        """Update what the user sees as their balance."""

        if elt is None:
            elt = self.Label_balance

        bal = str(self.game.kreds) + "kr"

        elt.config(text=bal, )

    def on_kreds_buy_change(self: Tk, event: Event):
        """Binding for the Kreds-to-money field needing to be updated."""

        elt: Entry = event.widget  # what triggered it

        try:
            val = int(elt.get())  # number of kreds they want
            cost = self.game.kredsToMoney(val)
            text = str(cost) + "$"

            self.Label_kreds_to_money.config(text=text)  # write it down
        except Exception as e:
            return  # do nothing if they type in some garbage

    def on_buy_kreds(self: Tk):
        """Binding for the 'Buy' button being clicked."""

        try:
            kreds = int(self.Entry_kreds.get())

            self.game.purchaseKreds(kreds)

            self.update_balance_view()

        except Exception as e:
            return  # quit if they enter wacky data

    def on_graph_click(self: Tk):
        """Binding for the 'Track Earnings' button being clicked."""
        pprint(self.game.transactionLog)  # TODO change this

        random_crate = random_item(list(self.game.itemcrates.values()))

        print("Random crate:")
        print(random_crate)

        self.set_crate_frame(random_crate)
