import pygame
from time import time
from display import DisplayObject
from Wave import Wave
import Colors

class Source(DisplayObject):
    def __init__(self, x, y, f):
        super().__init__(x, y)
        self.up = True
        self.count = 0
        self.max_count = round(1000 / f)

    def _vibe(self):
        wave = Wave(self.x, self.y, self.up)
        self.display.add(wave, -1)
        self.count = 0
        self.up = not self.up

    def on_add(self, display):
        super().on_add(display)
        self.count = 0

    def update(self):
        super().update()
        self.count += 1
        if self.count == self.max_count:
            self._vibe()

    def draw(self, surface):
        super().draw(surface)
        # gfxdraw.aacircle(surface, *circle, Colors.GRAY150)
        pygame.draw.circle(surface, Colors.BLUE, (self.x, self.y), 5)