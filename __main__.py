from pprint import *

from pygubu import *

from Game import *
from GuiLootItem import *
from LootItem import *
from guiLib import *
from GuiLootCrateGraph import *
from gui_pygubu import *

if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # don't show blank window

    app = MainGUI(root)
    graph = GuiLootCrateGraph(root)
    root.mainloop()
