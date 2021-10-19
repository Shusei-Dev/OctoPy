
from ursina import *

app = Ursina()

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = "quad"

if __name__ == "__main__":
    app.run()
