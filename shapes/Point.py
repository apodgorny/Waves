import pygame

from shapes.Shape import Shape

class Point(Shape):
    def __init__(self, x, y):
        self.x = round(x)
        self.y = round(y)

    def __getitem__(self, key):
        if   key == 0 : return self.x
        elif key == 1 : return self.y
        else: raise IndexError()

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def draw(self, surface, color, halfsize=1):
        pygame.draw.rect(surface, color, pygame.Rect(
            self.x - halfsize,
            self.y - halfsize,
            halfsize * 2,
            halfsize * 2
        ))