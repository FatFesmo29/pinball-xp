import pymunk

class PhysicsManager:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 980)  # g = 9.8 м/с² → 980 пикселей/с²

    def step(self, dt):
        self.space.step(dt)