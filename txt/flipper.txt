# game/flipper.py
import pygame
import pymunk

class Flipper:
    def __init__(self, space, x, y, angle=0, length=100, width=15, is_left=True):
        self.length = length
        self.width = width
        mass = 100
        moment = pymunk.moment_for_box(mass, (length, width))
        self.body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.body.angle = angle

        self.shape = pymunk.Poly.create_box(self.body, (length, width))
        self.shape.elasticity = 0.6
        self.shape.friction = 0.8
        self.shape.collision_type = 2  # для будущих коллизий, если нужно
        space.add(self.body, self.shape)

        # Закрепляем флиппер за одну точку (как шарнир)
        anchor = pymunk.PinJoint(space.static_body, self.body, (x, y), (0, 0))
        space.add(anchor)

        self.base_angle = angle
        self.active_angle = angle - (0.7 if is_left else -0.7)  # ~40 градусов в радианах
        self.is_active = False
        self.space = space

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def update(self, dt):
        target_angle = self.active_angle if self.is_active else self.base_angle
        current_angle = self.body.angle

        # Поворачиваем с ограничением скорости (чтобы не "ломать" физику)
        diff = target_angle - current_angle
        if abs(diff) > 0.01:
            # Устанавливаем угловую скорость пропорционально разнице
            self.body.angular_velocity = diff * 10  # настройте коэффициент (10–20)
        else:
            self.body.angle = target_angle
            self.body.angular_velocity = 0

    def draw(self, screen, ui):
        points = [ui.world_to_screen(*v) for v in self.shape.get_vertices()]
        pygame.draw.polygon(screen, (0, 180, 255), points)
        # Можно добавить чёрную обводку
        pygame.draw.polygon(screen, (0, 0, 0), points, 1)