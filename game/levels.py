# game/levels.py
from .flipper import Flipper
from .bumper import Bumper

class Level1:
    def __init__(self, physics, ui):
        self.physics = physics
        self.ui = ui
        self.bumpers = []
        self.flippers = []

        left_flipper = Flipper(physics.space, 400, 500, angle=-0.3, is_left=True)
        right_flipper = Flipper(physics.space, 600, 500, angle=0.3, is_left=False)
        self.flippers = [left_flipper, right_flipper]

        bumper1 = Bumper(physics.space, 500, 300, 20)
        self.bumpers.append(bumper1)

    def update(self, dt):
        for flipper in self.flippers:
            flipper.update(dt)

    def draw(self, screen):
        for bumper in self.bumpers:
            bumper.draw(screen, self.ui)
        for flipper in self.flippers:
            flipper.draw(screen, self.ui)