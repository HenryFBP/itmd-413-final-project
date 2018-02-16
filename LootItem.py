class LootItem:
    """
    A class representing a ``LootItem`` that can come from a ``LootCrate``.

    Attributes
        - ``name``      The name of the ``LootItem``.
        - ``rarity``    The weight to be multiplied into the chance that this ``LootItem`` will be selected.
    """

    name: str = "Loot Item"
    rarity: float = 0.5

    def __init__(self, name: str, rarity: float):
        self.name = name
        self.rarity = float(rarity)

    def __str__(self):
        return f"[{self.rarity*100:.8}%]: {self.name}"

    def __repr__(self):
        return str(self)
