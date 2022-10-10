import pygame, sys
from pygame.locals import *
import Colors

from display import DisplayObject

class Display:
    def __init__(self, w, h, caption, color):
        self.w, self.h = w, h
        self.objects = []

        pygame.init()
        pygame.display.set_caption(caption)

        self.surface = pygame.display.set_mode((w, h))
        self.surface.fill(color)
        self.can_play = True

    def add(self, o:DisplayObject, draw_priority=0):
        o.draw_priority = draw_priority
        self.objects.append(o)
        def sort_by(obj): return obj.draw_priority
        self.objects.sort(key=sort_by)
        o.on_add(self)

    def remove(self, o):
        self.objects.remove(o)
        o.on_remove()

    def update(self):
        for o in self.objects:
            if o.is_active():
                o.update()

    def draw(self):
        for o in self.objects:
            if o.is_visible():
                o.draw(self.surface)

    def size(self):
        return self.w, self.h

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()

            if self.can_play:
                self.surface.fill(Colors.BLACK)
                self.update()
                self.draw()

            # pygame.display.update()

    def pause(self):
        self.can_play = False

    def unpause(self):
        self.can_play = True

    def stop(self):
        pygame.quit()
        sys.exit()

    def in_range(self, x, y):
        return x in range(0, self.w) and y in range(0, self.h)