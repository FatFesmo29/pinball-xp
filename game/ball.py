import pygame
import pymunk

class Ball:
    def __init__(self, space, x, y, radius=10):
        self.radius = radius
        self.space = space
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius))
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.7
        self.shape.collision_type = 1
        space.add(self.body, self.shape)

    def reset_position(self, x, y):
        self.body.position = x, y
        self.body.velocity = (0,0)

    def draw(self, screen, ui):
        x, y = self.body.position
        sx, sy = ui.world_to_screen(x, y)
        pygame.draw.circle(screen, (255,60,60), (int(sx), int(sy)), int(self.radius * ui.scale))
