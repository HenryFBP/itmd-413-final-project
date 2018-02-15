class LootItem:
    """    A class representing a loot item that can come from a loot crate.

    Attributes
    ----------
        name : str      The name of the item.
        rarity : float  The weight to be multiplied into the chance that this item will be selected.
    """

    name = "Loot Item"
    rarity = 0.5

    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
