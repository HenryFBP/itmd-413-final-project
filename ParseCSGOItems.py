from pprint import *
import json


def parse(filepath: str = "_data/items_game_CSGO.json"):
    """
    Parses a CSGO JSON Dump file into a list of `LootItem` objects.
    :param filepath: The JSON file's location.
    :return: a list of `LootItem` objects.
    """

    file = open(filepath)
    json_data = json.load(file)

    pprint(json_data)

    d = {}


if __name__ == '__main__':
    parse()
