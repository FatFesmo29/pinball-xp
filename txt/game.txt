# game/game.py
import pygame
import pymunk
from .ui import UIManager
from .physics import PhysicsManager
from .levels import Level1
from .ball import Ball

class Game:
    def __init__(self):
        pygame.init()  # Хотя pygame уже инициализирован в main.py, дублирование безопасно
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height),
            pygame.RESIZABLE
        )
        pygame.display.set_caption("Pinball XP")

        self.clock = pygame.time.Clock()
        self.running = True

        # Менеджеры
        self.ui = UIManager(self.screen)
        self.physics = PhysicsManager()

        # === ДОБАВЛЕНИЕ ГРАНИЦ СТОЛА (очень важно!) ===
        self._add_table_walls()

        # Уровень (создаёт флипперы, бамперы и т.д.)
        self.level = Level1(self.physics, self.ui)

        # Шарик
        self.ball = Ball(self.physics.space, 400, 300, 10)

    def _add_table_walls(self):
        """Добавляет стены по краям игрового поля."""
        space = self.physics.space
        w, h = 1280, 720  # мировые координаты уровня (не экрана!)
        thickness = 20

        walls = [
            pymunk.Segment(space.static_body, (0, 0), (w, 0), thickness),       # верх
            pymunk.Segment(space.static_body, (0, h), (w, h), thickness),       # низ
            pymunk.Segment(space.static_body, (0, 0), (0, h), thickness),       # лево
            pymunk.Segment(space.static_body, (w, 0), (w, h), thickness),       # право
        ]
        for wall in walls:
            wall.elasticity = 0.8
            wall.friction = 0.5
        space.add(*walls)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # ~60 FPS

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE
                    )
                    self.ui.resize(event.w, event.h)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        if hasattr(self.level, 'flippers') and len(self.level.flippers) > 0:
                            self.level.flippers[0].activate()
                    elif event.key == pygame.K_RSHIFT:
                        if hasattr(self.level, 'flippers') and len(self.level.flippers) > 1:
                            self.level.flippers[1].activate()
                    elif event.key == pygame.K_SPACE:
                        # Временный ланчер: выстрел вверх
                        self.ball.body.velocity = (0, -400)

                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                        for flipper in getattr(self.level, 'flippers', []):
                            flipper.deactivate()

            # Обновление физики и логики
            self.physics.step(dt)
            if hasattr(self.level, 'update'):
                self.level.update(dt)

            # Отрисовка
            self.screen.fill((10, 10, 30))
            if hasattr(self.level, 'draw'):
                self.level.draw(self.screen)
            self.ball.draw(self.screen, self.ui)
            pygame.display.flip()

        pygame.quit()