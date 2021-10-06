import sys
import pygame as pg
from .settings import *
from .ui import *
from .grid import Graph


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode(SIZE, 0, 32)
        self.clock = pg.time.Clock()

        # UI
        self.instructions = Button("Instructions", (100, 30), (10, 10))
        self.instructions.on_click(self.show_instructions)
        
        # Navigation Graph
        self.graph = Graph((600, 500), (50, 150))

    def show_instructions(self):
        self.inst = not self.inst

    def show_settings(self):
        self.sett = not self.sett
