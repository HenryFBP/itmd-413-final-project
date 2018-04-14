import json
from datetime import time

from LootCrate import LootCrate
from LootItem import LootItem


class Game:
    """

    Attributes
        - ``kredsratio``        How many kreds you get per dollar.
        - ``rarities``          List of rarities.
        - ``itempool``          List of all available items.
        - ``itemgroups``        List of groups of items, to be used in crates for convenience.
        - ``itemcrates``        List of all item crates.

        - ``kreds``             User's kreds.
        - ``inventory``         User's owned items.
        - ``crates``            User's owned, unopened crates.


        A class that facilitates/organizes the following:

    - Currency
        - Purchasing/using currency
        - Keeping track of the player's currency

    - LootCrate objects
        - Registering LootCrate objects
        - Deciding what items a LootCrate object will contain

    - Having a master list of all items
        - Indexing an item by an attribute (name, rarity, etc)
        - Keeping a transaction log and changelog
    """

    def __init__(self, kredsratio=10, kreds=None):
        """
        :param kredsratio: How many kreds per dollar. 10 by default.
        :param kreds How many kreds the user starts with. 10$ worth by default.
        """

        if kreds is None:
            kreds = 10 * kredsratio  # 10$ worth

        self.kredsratio = kredsratio
        self.rarities = []
        self.transactionLog = []
        self.itempool = []
        self.itemgroups = {}
        self.itemcrates = {}

        self.kreds = kreds
        self.inventory = []
        self.crates = {}

    def kredsToMoney(self, kreds):
        """
        Given ``kreds``, converts them into dollars.
        """
        return kreds / self.kredsratio

    def moneyToKreds(self, dollars):
        """
        Given ``dollars``, converts them into Kreds.
        """
        return self.kredsratio * dollars

    def itemByName(self, name):
        """
        Given a ``name``, return an item with that ``name``.
        """
        for item in self.itempool:
            if item.name == name:
                return item

        print("No item by '"+name+"' found!")

        return None

    def logPurchaseKreds(self, kreds, dollars):
        """
        Log that we purchased ``kreds`` for some amount of ``dollars``.
        """
        self.transactionLog.append({self.purchaseKreds.__name__: {
            "time": time.time(),
            "kreds": kreds,
            "dollars": dollars,
            "balance": self.kreds,
        }})

    def purchaseKreds(self, k):
        """Add ``k`` kreds to the Game's balance.
        This costs money."""
        dollars = k / self.kredsratio

        self.logPurchaseKreds(k, dollars)

        self.kreds += k
        return

    def import_rarities(self, path):
        """
        Parse a JSON file representing rarities of items.
        """
        d = {}

        with open(path) as json_data:
            d = json.load(json_data)

            json_data.close()

        self.rarities += d

        return d

    def import_items(self, path):
        """
        Parse a JSON file representing a list of items.
        """

        d = {}
        items = []

        with open(path) as json_data:
            d = json.load(json_data)

            json_data.close()

        for name in d:
            json_item = {name: d[name]}
            item = LootItem.from_dict(json_item)
            items.append(item)

        self.itempool += items

        # for item in self.itempool:
        #     print(item)

        return items

    def import_groups(self, path):
        """
        Parse a JSON file representing a list of item groups.
        """

        d = {}
        groups = {}

        with open(path) as json_data:
            d = json.load(json_data)

            json_data.close()

        for jgname in d:  # for group X
            jgroup = d[jgname]
            items = []  # make a new list for a group name

            for jiname in jgroup:  # for all items in group X
                item = self.itemByName(jiname)
                items.append(item)  # add the item object

            groups[jgname] = items  # add our single group w/ items
            self.itemgroups[jgname] = items

        return groups

    def import_crates(self, path):
        """
        Parse a JSON file representing a list of item crates.
        """
        d = {}
        crates = {}

        with open(path) as json_data:
            d = json.load(json_data)

            json_data.close()

        # print("All jcrates")
        # print(d)

        for crateName in d:  # go through all crates
            jcrate = d[crateName]
            capacity = jcrate['capacity']
            cost = jcrate['cost']

            # print(f"'{crateName}'-named crate:")
            # print(jcrate)

            items = []  # items for one crate
            for groupName in jcrate['groups']:  # go through all groups
                items += self.itemgroups[groupName]  # add that group's items

            for itemName in jcrate['items']:  # go through just items
                items.append(self.itemByName(itemName))  # add that item

            crate = LootCrate(crateName, cost, items, capacity)  # make a new Crate object

            # print('crate object:')
            # print(str(crate))

            crates[crateName] = crate
            self.itemcrates[crateName] = crate

        return crates

    def ncrateidx(self):
        """Normalize crate index."""
        if hasattr(self, '_crate_idx'):

            if self._crate_idx < 0:
                self._crate_idx += len(self.itemcrates.values())  # normalize up

            elif self._crate_idx >= len(self.itemcrates.values()) - 1:
                self._crate_idx -= len(self.itemcrates.values())  # normalize down
        else:
            self._crate_idx = 0

    def cycleLeft(self):
        """ Cycles Crates Left and returns the crate"""

        self.ncrateidx()
        self._crate_idx -= 1

        print("Current idx is " + str(self._crate_idx))

        allcrates = list(self.itemcrates.values())
        acrate = allcrates[self._crate_idx]

        print("total crates:")
        print(len(allcrates))

        return acrate

    def cycleRight(self):
        """ Cycles Crates Left and returns the crate"""
        self.ncrateidx()
        self._crate_idx += 1

        print("Current idx is " + str(self._crate_idx))

        allcrates = list(self.itemcrates.values())
        acrate = allcrates[self._crate_idx]

        return (acrate)
