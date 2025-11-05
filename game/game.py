import pygame
from .ui import UIManager
from .physics import PhysicsManager
from .levels import Level1
from .ball import Ball

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        pygame.display.set_caption("Pinball XP")
        self.clock = pygame.time.Clock()
        self.running = True

        # Загрузка фона уровня
        self.background = pygame.image.load("assets/space_background.png").convert()

        self.ui = UIManager(self.screen)
        self.physics = PhysicsManager()

        self._add_walls()

        self.level = Level1(self.physics, self.ui)
        self.ball = Ball(self.physics.space, 640, 50, 10)

        self._setup_collision()

    def _add_walls(self):
        # Добавляем стены
        w, h = 1280, 720
        thickness = 20
        s = self.physics.space
        walls = [
            # По периметру
            pygame.math.Vector2(0, 0), pygame.math.Vector2(w, 0),
            pygame.math.Vector2(0, h), pygame.math.Vector2(w, h),
        ]
        # Объявляем стены
        static_body = s.static_body
        segs = [
            pygame.math.Vector2(0, 0), pygame.math.Vector2(w, 0),
            pygame.math.Vector2(0, 0), pygame.math.Vector2(0, h),
            pygame.math.Vector2(w, 0), pygame.math.Vector2(w, h),
            pygame.math.Vector2(0, h), pygame.math.Vector2(w, h),
        ]
        for i in range(0, len(segs), 2):
            seg = pymunk.Segment(static_body, segs[i], segs[i+1], thickness)
            seg.elasticity = 0.8
            seg.friction = 0.5
            s.add(seg)

    def _setup_collision(self):
        self.physics.space.add_collision_handler(1, 3).post_solve = self._on_target_hit

    def _on_target_hit(self, arbiter, space, data):
        self.ui.score += arbiter.shapes[1].target_points
        return True

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.ui.resize(event.w, event.h)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.reset_position(640, 50)

            self.physics.step(dt)
            self.level.update(dt)

            self.screen.blit(self.background, (0,0))
            self.level.draw(self.screen)
            self.ball.draw(self.screen, self.ui)
            self.ui.draw_score()
            self.ui.draw_mission()

            pygame.display.flip()
        pygame.quit()
