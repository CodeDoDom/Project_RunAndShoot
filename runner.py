from pico2d import load_image


class Runner:
    def __init__(self):
        self.x, self.y = 450, 300
        self.frame = 0
        self.action = 3
        self.image = load_image('Boy_animation.png')

    def draw(self):
        self.draw(self.x, self.y)
