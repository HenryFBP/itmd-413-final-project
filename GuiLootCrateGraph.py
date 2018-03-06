from pprint import *
import matplotlib as mpl
import numpy as np
import tkinter as tk

from pygubu import *

from Game import *
from GuiLootItem import *
from GuiLootCrateGraph import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import matplotlib.pyplot as plt


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo


class GuiLootCrateGraph:

    def __init__(self, master, path='./gui_graph.ui'):
        # 1: Create a builder
        self.builder = Builder()

        # 2: Load an ui file
        self.builder.add_from_file(path)

        # 3: Create the widget using a master as parent
        self.mainwindow: Toplevel = self.builder.get_object('mainwindow', master)

        # get canvas object for GRAFFIN STUFF
        self.canvas: Canvas = self.builder.get_object('CanvasGraph', master)

        # generate example data
        X = np.linspace(0, 2, 50)
        Y = np.sin(X)

        # Create the figure we desire to add to an existing canvas
        fig = mpl.figure.Figure(figsize=(2, 1))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.plot(X, Y)

        # Keep this handle alive, or else figure will disappear
        fig_x, fig_y = 100, 100
        fig_photo = draw_figure(self.canvas, fig, loc=(fig_x, fig_y))
        fig_w, fig_h = fig_photo.width(), fig_photo.height()

        # Add more elements to the canvas, potentially on top of the figure
        self.canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
        self.canvas.create_text(200, 50, text="Zero-crossing", anchor="s")