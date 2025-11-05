import pygame
import pymunk
from .target import Target

class Level1:
    def __init__(self, physics, ui):
        self.physics = physics
        self.ui = ui
        self.targets = []

        # Заготовка для целей (таргеты)
        self.targets.append(Target(self.physics.space, 300, 200))
        self.targets.append(Target(self.physics.space, 500, 200))
        self.targets.append(Target(self.physics.space, 700, 200))
        # Можно заменить на графику или добавить еще объектов

    def update(self, dt):
        pass

    def draw(self, screen):
        for t in self.targets:
            t.draw(screen, self.ui)
