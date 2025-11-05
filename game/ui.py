import pygame

class UIManager:
    def __init__(self, screen, world_width=1280, world_height=720):
        self.screen = screen
        self.world_width = world_width
        self.world_height = world_height
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self._update_scale()

        self.score = 0
        self.mission_text = "Hit Targets To Start"

    def resize(self, w, h):
        self.screen_width = w
        self.screen_height = h
        self._update_scale()

    def _update_scale(self):
        scale_x = self.screen_width / self.world_width
        scale_y = self.screen_height / self.world_height
        self.scale = min(scale_x, scale_y)
        self.offset_x = (self.screen_width - self.world_width * self.scale) / 2
        self.offset_y = (self.screen_height - self.world_height * self.scale) / 2

    def world_to_screen(self, x, y):
        sx = self.offset_x + x * self.scale
        sy = self.offset_y + y * self.scale
        return int(sx), int(sy)

    def draw_score(self):
        font = pygame.font.SysFont('Arial', 24)
        text_surface = font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(text_surface, (10, 10))

    def draw_mission(self):
        font = pygame.font.SysFont('Arial', 24)
        text_surface = font.render(self.mission_text, True, (255,255,255))
        self.screen.blit(text_surface, (10, 40))
