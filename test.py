
from ursina import *

app = Ursina()

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = "quad"

    def update(self):
        self.x += 0.01

if __name__ == "__main__":
    player = Player()
    app.run()
