# game/bumper.py
import pygame
import pymunk

class Bumper:
    def __init__(self, space, x, y, radius=20):
        self.radius = radius
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1.2  # >1 — даёт "пружинистый" отскок
        self.shape.friction = 0.0
        space.add(self.body, self.shape)

    def draw(self, screen, ui):
        x, y = self.body.position
        sx, sy = ui.world_to_screen(x, y)
        scaled_radius = int(self.radius * ui.scale)
        pygame.draw.circle(screen, (255, 215, 0), (sx, sy), scaled_radius)  # золотой цвет