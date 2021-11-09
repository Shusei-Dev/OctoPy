

class StateManager:

    def __init__(self):

        # 0 = Quit, 1 = Menu, 2 = Settings, 3 = PlayList, 4 = Play
        self.game_state = 1

    def change_game_state(self, state):

        if state in [0, 1, 2, 3, 4]:
            self.game_state = state

    def get_game_state(self):
        return self.game_state
