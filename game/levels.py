# game/levels.py
class Level1:
    def __init__(self, physics, ui):
        self.physics = physics
        self.ui = ui
        self.bumpers = []
        self.flippers = []

        # Добавляем флипперы
        left_flipper = Flipper(physics.space, 400, 500, angle=-45)
        right_flipper = Flipper(physics.space, 600, 500, angle=45)
        self.flippers = [left_flipper, right_flipper]

        # Добавляем бамперы
        bumper1 = Bumper(physics.space, 500, 300, 20)
        self.bumpers.append(bumper1)

    def draw(self, screen):
        for bumper in self.bumpers:
            bumper.draw(screen, self.ui)
        for flipper in self.flippers:
            flipper.draw(screen, self.ui)