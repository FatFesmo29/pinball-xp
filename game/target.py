import pygame
import pymunk

class Target:
    def __init__(self, space, x, y, size=20, points=100):
        self.points = points
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, size/2)
        self.shape.elasticity = 1.2
        self.shape.collision_type = 3
        space.add(self.body, self.shape)

    def draw(self, screen, ui):
        x, y = self.body.position
        sx, sy = ui.world_to_screen(x, y)
        rect = self.image.get_rect(center=(sx, sy))
        screen.blit(self.image, rect)
