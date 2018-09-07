class GameEngine:
    """Class for holding current game state and log of the adventure"""
    def __init__(self, story_dir="christmas18"):
        self.phase = 1
        self.story_dir = story_dir

    def logit(self, message):
        with open('game.log', "a") as f:
            f.write(message)
