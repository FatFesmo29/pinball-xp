import pymunk

class Flipper:
    def __init__(self, space, x, y, angle=0, length=100, width=10):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (length, width))
        self.shape.friction = 0.8
        self.shape.elasticity = 0.6
        space.add(self.body, self.shape)

        # Сустав для вращения
        self.joint = pymunk.RotaryLimitJoint(space.static_body, self.body, 0, 0)
        self.angle = angle
        self.max_angle = 45  # градусов
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def update(self, dt):
        if self.active:
            target_angle = self.max_angle
        else:
            target_angle = 0

        # Плавное вращение
        current_angle = self.body.angle
        diff = target_angle - current_angle
        if abs(diff) > 0.1:
            self.body.angle += diff * 0.1
        else:
            self.body.angle = target_angle