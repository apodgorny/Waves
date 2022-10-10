from shapes.Line import Line

class DisplayObject:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.animator = None
        self.display = None
        self.draw_priority = 0

    def move_to(self, x, y):
        if x is not None: self.x = x
        if y is not None: self.y = y

    def animate_to(self, x, y, step):
        self.animator = Line(self.x, self.y, x, y).animator(step)

    def animate(self):
        if self.animator:
            try:
                point = next(self.animator)
                if point:
                    self.move_to(*point)
            except StopIteration:
                self.animator = None
                return False
        return True

    def draw(self, surface):
        pass

    def update(self):
        if self.animator:
            self.animate()

    def position(self):
        return self.x, self.y

    def is_active(self):
        return True

    def is_visible(self):
        return True

    def on_add(self, display):
        self.display = display

    def on_remove(self):
        pass

