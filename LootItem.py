class LootItem:
    """
    A class representing a ``LootItem`` that can come from a ``LootCrate``.

    Attributes
        - ``name``      The name of the ``LootItem``.
        - ``rarity``    The weight to be multiplied into the chance that this ``LootItem`` will be selected.
    """

    name: str = "Loot Item"
    rarity: float = 0.50
    type: str = "weapon"
    worth: float = 0.10

    def __init__(self, name: str, rarity: float, type: str, worth: float = 0.0):
        self.name = name
        self.rarity = rarity
        self.type = type
        self.worth = float(worth)

    def __str__(self):
        ret = f"[{self.rarity:^10}]: {self.type:13} {self.name:25}"

        if self.worth != 0.0:  # if it has a price
            ret += f" at ${self.worth:<10}"

        return ret

    def __repr__(self):
        return str(self)

    @staticmethod
    def from_dict(d):
        name = list(d.keys())[0]
        item = d[name]

        rarity = item["rarity"]
        worth = item["worth"]
        type = item["type"]

        return LootItem(name, rarity, type, worth)
