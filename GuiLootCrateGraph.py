from pprint import *

from pygubu import *

from Game import *
from GuiLootItem import *
from GuiLootCrateGraph import *

class GuiLootCrateGraph:
    def __init__(self, master, path='./gui_graph.ui'):
        # 1: Create a builder
        self.builder = Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)
