import json

from LootItem import *


class CSGOParser:
    dictionary = None
    rarities = None
    jitems = None
    items = []

    def __init__(self, filepath: str):
        """
        Initialize ``self`` with JSON data located at ``filepath``.

        :param filepath: The location of the JSON datafile.
        """
        dictionary = self.parse(filepath)

        self.dictionary = dictionary
        self.rarities = dictionary["rarities"]
        self.qualities = dictionary["qualities"]
        self.jitems = dictionary["items"]

        # print("Items:")
        # pprint(self.jitems)

        # go through all JSON objects
        for item_id in self.jitems:
            jitem = self.jitems[item_id]
            item = self.jitem_to_item(jitem)

            # if item exists
            if item:
                self.items.append(item)
                print(item, end="\n\n")

    def item_weight(self, jitem: dict) -> int:
        """
        Get the weight for a JSON item.

        :param jitem: A JSON item.
        :return: The weight associated with this item.

        Large weights are more common, small weights are less common.
        """
        if "item_quality" in jitem:
            return self.quality_to_weight(jitem)
        elif "item_rarity" in jitem:
            return self.rarity_to_weight(jitem)

        return 0

    def item_percent(self, jitem: dict) -> float:
        """
        Get the percent for a JSON item.

        :param jitem: A JSON item.
        :return: The percentage chance to get with this item.
        """
        weight = total = None
        percent = 0

        # higher weight means LOWER chance
        if "item_quality" in jitem:
            weight = self.quality_to_weight(jitem["item_quality"])
            total = self.total_qualities()
            percent = 1 / weight

            # print(f"Quality: higher weight means LOWER chance.")
            # print(f"{weight} weight, {total} total.")
            # print("1 / weight = percent")
            # print(f"{1} / {weight} = {percent}")

        # higher weight means larger chance
        elif "item_rarity" in jitem:
            weight = self.rarity_to_weight(jitem["item_rarity"])
            total = self.total_rarities()
            percent = weight / total

            # print(f"Rarity: higher weight means LARGER chance")
            # print(f"{weight} weight, {total} total.")
            # print("weight / total = percent")
            # print(f"{weight} / {total} = {percent}")

        return percent

    def total_rarities(self) -> int:
        """
        Get all rarity weights summed up.

        :return: The sum of all weight values for all rarities.
        """
        total = 0

        for rarity in self.rarities:
            if "weight" in self.rarities[rarity]:
                print(f"Rarity {rarity} is {self.rarities[rarity]['weight']}")
                total += int(self.rarities[rarity]["weight"])

        # print(f"Total rarities: {total}")
        return total

    def total_qualities(self) -> int:
        """
        Get all quality weights summed up.

        :return: The sum of all weight values for all qualities.
        """
        total = 0

        for quality in self.qualities:
            if "weight" in self.qualities[quality]:
                # print(f"Quality {quality} is {self.qualities[quality]['weight']}")
                total += int(self.qualities[quality]["weight"])

        # print(f"Total qualities: {total}")
        return total

    def rarity_to_weight(self, rarity: str) -> int:
        """
        Turn an ``item_rarity`` into a weight value.

        :param rarity: The string representing a rarity.
        :return: The weight associated with the string.

        Example:\n
        ``rarity_to_weight("common") -> 10000000``\n
        ``rarity_to_weight("mythical") -> 80000``\n
        """

        try:
            return int(self.rarities[rarity]["weight"])
        except Exception:
            pass

        return 0

    def quality_to_weight(self, quality: str) -> int:
        """
        Turn an ``item_quality`` into a weight value.

        :param rarity: The string representing a quality.
        :return: The weight associated with the string.

        Example:\n
        ``quality_to_weight("normal") -> 0``\n
        ``quality_to_weight("genuine") -> 30``\n
        """

        try:
            return int(self.qualities[quality]["weight"])
        except Exception:
            pass

        return 0

    def jitem_to_item(self, jitem: dict) -> LootItem:
        """
        Parses a single CSGO JSON item into a ``LootItem.``\n
        Returns ``None`` upon failure.

        :param jitem: A CSGO JSON item.
        :return: A ``LootItem.``
        """
        print(jitem)

        if "name" in jitem:
            name = jitem["name"]

        # return None if JSON item doesn't have these vars
        try:
            name
        except NameError:
            return None

        percent = self.item_percent(jitem)

        item = LootItem(name, percent)

        return item

    def parse(self, filepath: str) -> {}:
        """
        Parses a CSGO JSON Dump file into a list of ``LootItem`` objects.

        :param filepath: The JSON file's location.
        :return: a list of ``LootItem`` objects.
        """

        file = open(filepath)
        json_data = json.load(file)

        # pprint(json_data)

        return json_data


if __name__ == '__main__':
    csgo = CSGOParser("_data/items_game_CSGO.json")
