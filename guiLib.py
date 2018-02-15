import random

from LootItem import *

hex_digits = "0123456789ABCDEF"

modifiers = ["bad", "ok", "good", "awesome", "godly"]
types = ["sword", "gun", "churro", "noodle", "shield"]
conjs = ["of", "in", "with", "without", "having", "derived from", "inside of", "outside of"]
attrs = ["justice", "evil", "zits", "pastries", "noodle-osity", "helplessness", "body odor"]


def random_item(list):
    """Return a random item in list ``list`` between ``0`` and ``len(list)``. """
    return list[random.randrange(0, len(list))]


def randomLootItem() -> LootItem:
    name = f"{random_item(modifiers)} {random_item(types)} {random_item(conjs)} {random_item(attrs)}"
    rarity = random.uniform(0, 1)

    return LootItem(name, rarity)


def random_hex_digit():
    """
    Return a random single-digit hex string.
    :return: The hex string.
    Example:
    r_h_d() -> "E"
    """
    return random_item(hex_digits)


def random_hex_string(l=6):
    """
    Return a random hex color string.
    :param l: How long the hex string will be.
    :return: The hex string.
    Example:
    r_h_s(l=3) -> "A0E"
    r_h_s(l=1) -> "F"
    """
    return ''.join([random_hex_digit() for i in range(l)])
