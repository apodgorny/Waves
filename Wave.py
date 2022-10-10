import math
import pygame

from display import DisplayObject
import Colors

class Wave(DisplayObject):
    def __init__(self, x, y, up=True, v=1):
        super().__init__(x, y)
        self.up, self.v = up, v
        self.r = 0
        self.max_r = 0
        self.draw_circles = False

    def on_add(self, display):
        super().on_add(display)
        xlen = self.x
        if self.x < self.display.w / 2:
            xlen = self.display.w - self.x
        ylen = self.y
        if self.y < self.display.h / 2:
            ylen = self.display.h - self.y
        self.max_r = math.sqrt(xlen**2 + ylen**2)

    def on_remove(self):
        del self

    def is_visible(self):
        return self.r < self.max_r + 50

    def update(self):
        if self.is_visible():
            self.r += self.v
        else:
            self.display.remove(self)

    def draw(self, surface):
        color = Colors.GRAY200 if self.up else Colors.GRAY50
        if self.draw_circles:
            pygame.draw.circle(surface, color, (self.x, self.y), self.r, 2)