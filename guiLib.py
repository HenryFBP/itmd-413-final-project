import random
from pprint import *

from LootItem import *

hex_digits = "0123456789ABCDEF"

modifiers = ["bad", "ok", "good", "awesome", "godly"]
types = ["sword", "gun", "churro", "noodle", "shield"]
conjs = ["of", "in", "with", "without", "having", "derived from", "inside of", "outside of"]
attrs = ["justice", "evil", "zits", "pastries", "noodle-osity", "helplessness", "body odor"]


def printif(*thing, b=False):
    """
    Print ``thing`` if ``b`` is true

    :param thing: The thing.
    :param b: The condition.

    :return: None
    """
    if (b):
        print(*thing)


def random_item(list):
    """
    Randomly select an element from ``list``.

    :return: Return a random item in list ``list`` between ``0`` and ``len(list)``.
    """
    return list[random.randrange(0, len(list))]


def randomLootItem() -> LootItem:
    """
    Generate a random ``LootItem`` object.

    :return: A random ``LootItem``.
    """
    name = f"{random_item(modifiers)} {random_item(types)} {random_item(conjs)} {random_item(attrs)}"
    rarity = random.uniform(0, 1)

    return LootItem(name, rarity)


def random_hex_digit():
    """
    Return a random single-digit hex string.

    :return: The hex string.

    Example:
    ``random_hex_digit() -> "E"``
    """
    return random_item(hex_digits)


def random_hex_string(l=6):
    """
    Return a random hex color string.

    :param l: How long the hex string will be.
    :return: The hex string.

    Example:
    ``random_hex_string(l=3) -> "A0E"``
    ``random_hex_string(l=1) -> "F"``
    """
    return ''.join([random_hex_digit() for i in range(l)])


# https://csgostash.com/img/skins/large_1920/s500.png
# https://csgostash.com/img/containers/c238.png
def generate_URLS(url: str = "https://csgostash.com/img/skins/large_1920/s", times: int = 1000, suffix: str = ".png"):
    """
    Generate a list of icon URLs.

    :param url: The prefix to apply to the URL.
    :param times: How many URLs to generate.
    :param suffix: The file suffix to apply to the URL.
    :return: A list of URL strings that probably have images.
    """
    urls = []

    for i in range(times):
        urls.append(url + str(i) + suffix)

    return urls


def save_URL_to_file(url: str, filepath: str) -> None:
    """
    Save the content located at ``url`` to a file located at ``filepath``.
    :param url:
    :param filepath:
    :return:
    """


def generate_URL_file(urls: list, path: str = "./_data/icon_URLs/", name: str = "testlist", ext: str = ".txt") -> None:
    """
    Save ``urls`` to a file.

    :param urls: The list of URLs.
    :param path: The path for the ``urls`` file to be saved.
    :param name: The name of the file.
    :param ext: The extension of the file.
    """
    f = open(path + name + ext, "w")

    for url in urls:
        f.write(url + "\r\n")

    f.close()


def generate_all_URLs():
    """
    Generate all URL list files that reference images.
    """

    generate_URL_file(generate_URLS("https://csgostash.com/img/skins/large_1920/s"), name="skins")
    generate_URL_file(generate_URLS("https://csgostash.com/img/containers/c"), name="containers")

def main():
    """
    Interactive function-list REPL for doing various maintenance tasks.
    """
    callbacks = {
        "quit": lambda: exit(0),
        "urls": generate_all_URLs,
    }

    while True:
        print("options: ")
        pprint(callbacks)

        inp = input(" > ")

        if inp in callbacks:
            print(f"Running {callbacks[inp].__name__}()...")
            callbacks[inp]()  # call what they specify
        else:
            print(f"'{inp}' not in callback list!")


if __name__ == "__main__":
    main()