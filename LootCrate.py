import numpy as np

from guiLib import *


class LootCrate:
    """
    A class representing a single loot crate that can have multiple items.

    Attributes
        - ``name``:         The name of the ``LootCrate``.
        - ``cost``:         The cost of the ``LootCrate``.
        - ``pool``:         The pool of items that could appear inside of the ``LootCrate``.
        - ``capacity``:     The amount of items this ``LootCrate`` will give you.
    """

    name = "Default Loot Crate"
    cost = 10
    pool = [randomLootItem() for i in range(10)]
    capacity = 3
    opened = False

    def __init__(self, name: str = name, cost: float = cost, pool: list = pool, capacity: int = capacity):
        self.name = name
        self.cost = cost
        self.pool = pool
        self.capacity = capacity

    def open(self):
        """
        Opens a ``LootCrate``.

        See https://stackoverflow.com/a/39976962.\n
        The contents are determined by weighted random choices
        over all of ``self.pool``.\n

        :return: A list of ``LootItem`` objects.
        """

        weights = [item.rarity for item in self.pool]  # does not sum to one

        normalizedWeights = np.array(weights)
        normalizedWeights /= normalizedWeights.sum()  # this does

        items = np.random.choice(self.pool, self.capacity, replace=False, p=normalizedWeights)

        return items

    def __iter__(self):
        return self.pool.__iter__()

    def __str__(self):
        ret = ""

        ret += f"{self.capacity:2} items from '{self.name}' at ${self.cost}:\n"

        for item in self.pool:
            ret += str(item) + "\n"

        return ret

    def __repr__(self):
        return str(self)


def test():
    """
    Test out the functionality of our ``LootCrate`` class.
    """
    crate = LootCrate()

    print("Crate's items: ")
    for item in crate: print(item)

    print("")
    print(f"{crate.capacity} random items:")
    for item in crate.open(): print(item)


if __name__ == '__main__':
    test()
