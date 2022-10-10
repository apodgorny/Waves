import pygame
import Colors
from library import get_intersection
from display import DisplayObject
from Wave import Wave

class Waves(DisplayObject):
    def __init__(self):
        super().__init__(0, 0)
        self.highs = []
        self.lows = []
        self.zeroes = []
        self.a = []
        self.waves = []
        self.pixarray = None

    def _clear(self):
        for x in range(self.display.w):
            for y in range(self.display.h):
                self.a[x][y] = 0

    def on_add(self, display):
        super().on_add(display)
        for x in range(display.w):
            self.a.append([])
            for y in range(display.h):
                self.a[x].append(0)

    def update(self):
        total_resonance = 0
        self.pixarray = pygame.PixelArray(self.display.surface)
        for item1 in self.display.objects:
            if isinstance(item1, Wave):
                for item2 in self.display.objects:
                    if isinstance(item2, Wave):
                        intersection = get_intersection(
                            item1.x, item1.y, item1.r,
                            item2.x, item2.y, item2.r
                        )
                        if intersection:
                            x1, y1, x2, y2 = intersection
                            resonance = pygame.Color('green')
                            if item1.up != item2.up:
                                resonance = pygame.Color('red')

                            if self.display.in_range(x1, y1):
                                self.pixarray[x1][y1] = resonance

                            if self.display.in_range(x2, y2):
                                self.pixarray[x2][y2] = resonance

                            # total_resonance += resonance

        # print(total_resonance)

    def draw(self, surface):
        # for x in range(self.display.w):
        #     for y in range(self.display.h):
        #         if self.a[x][y] > 0:
        #             surface.set_at((x, y), Colors.GREEN)
        #         elif self.a[x][y] < 0:
        #             surface.set_at((x, y), Colors.RED)
        pygame.surfarray.blit_array(surface, self.pixarray)
        pygame.display.flip()




