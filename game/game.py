import pygame
import pymunk
from .ui import UIManager
from .physics import PhysicsManager
from .levels import Level1
from .ball import Ball
from .flipper import Flipper
from .bumper import Bumper

class Game:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Pinball XP")

        self.clock = pygame.time.Clock()
        self.running = True

        # Менеджеры
        self.ui = UIManager(self.screen)
        self.physics = PhysicsManager()

        # Уровень
        self.level = Level1(self.physics, self.ui)

        # Шарик
        self.ball = Ball(self.physics.space, 400, 300, 10)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # delta time в секундах

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.ui.resize(event.w, event.h)

            # Обновление физики
            self.physics.step(dt)

            # Отрисовка
            self.screen.fill((0, 0, 0))
            self.level.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()

        pygame.quit()