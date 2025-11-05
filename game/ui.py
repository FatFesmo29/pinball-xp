import pygame

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.scale = 1.0
        self.offset_x = 0
        self.offset_y = 0

    def resize(self, w, h):
        self.width = w
        self.height = h
        # Можно пересчитать scale, если нужно адаптировать под уровень
        # Например: self.scale = min(w / 1280, h / 720)

    def world_to_screen(self, x, y):
        # Преобразование координат мира в экран
        return int(x * self.scale + self.offset_x), int(y * self.scale + self.offset_y)

    def draw_circle(self, color, x, y, radius):
        sx, sy = self.world_to_screen(x, y)
        sr = int(radius * self.scale)
        pygame.draw.circle(self.screen, color, (sx, sy), sr)