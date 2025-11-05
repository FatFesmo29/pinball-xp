# game/ball.py
import pygame
import pymunk

class Ball:
    def __init__(self, space, x, y, radius=10):
        self.radius = radius
        mass = 1
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.7
        space.add(self.body, self.shape)

    def draw(self, screen, ui):
        x, y = self.body.position
        sx, sy = ui.world_to_screen(x, y)
        pygame.draw.circle(screen, (255, 60, 60), (int(sx), int(sy)), int(self.radius * ui.scale))