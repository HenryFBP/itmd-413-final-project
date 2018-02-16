class LootItem:
    """    A class representing a loot item that can come from a loot crate.

    Attributes
    ----------
        name : str      The name of the item.
        rarity : float  The weight to be multiplied into the chance that this item will be selected.
    """

    name: str = "Loot Item"
    rarity: float = 0.5

    # array = [1,2,3,4,"hi mom!"]

    def __init__(self, name: str, rarity: float):
        """
        Make a new `LootItem`.

        :param name The name of the `LootItem`.
        :param rarity The weight to be multiplied into the chance that this item will be selected.
        """
        self.name = name
        self.rarity = float(rarity)

        return

    def __str__(self):
        return f"[{self.rarity:.2}]: {self.name}"

    def __repr__(self):
        return str(self)