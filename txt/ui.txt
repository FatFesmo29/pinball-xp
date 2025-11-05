# game/ui.py
import pygame

class UIManager:
    def __init__(self, screen, world_width=1280, world_height=720):
        self.screen = screen
        self.world_width = world_width
        self.world_height = world_height
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self._update_scale()

    def resize(self, w, h):
        """Вызывается при изменении размера окна."""
        self.screen_width = w
        self.screen_height = h
        self._update_scale()

    def _update_scale(self):
        """Рассчитывает масштаб так, чтобы весь мир помещался в окно."""
        # Сохраняем пропорции мира: не растягиваем, добавляем чёрные полосы при необходимости
        scale_x = self.screen_width / self.world_width
        scale_y = self.screen_height / self.world_height
        self.scale = min(scale_x, scale_y)  # масштаб, при котором мир целиком виден

        # Центрируем мир на экране
        self.offset_x = (self.screen_width - self.world_width * self.scale) / 2
        self.offset_y = (self.screen_height - self.world_height * self.scale) / 2

    def world_to_screen(self, x, y):
        """Преобразует мировые координаты в экранные."""
        sx = self.offset_x + x * self.scale
        sy = self.offset_y + y * self.scale
        return int(sx), int(sy)

    def draw_circle(self, color, x, y, radius):
        """Универсальный метод отрисовки круга с масштабированием."""
        sx, sy = self.world_to_screen(x, y)
        scaled_radius = int(radius * self.scale)
        pygame.draw.circle(self.screen, color, (sx, sy), scaled_radius)

    def draw_polygon(self, color, vertices):
        """Отрисовка многоугольника с масштабированием."""
        screen_vertices = [self.world_to_screen(x, y) for x, y in vertices]
        pygame.draw.polygon(self.screen, color, screen_vertices)