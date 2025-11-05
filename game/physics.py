import pymunk

class PhysicsManager:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 980)

    def step(self, dt):
        self.space.step(dt)
