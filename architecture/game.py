class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, story_dir="christmas18"):
        self.phase = 1
        self.story_dir = story_dir
        self.index = 1
        self.answer_set = {}

    def get_current_story(self):
        pass

    def check_answer(self, answer):
        pass

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_file = 'The_Story_Thus_Far.log' if public else 'internal.log'
        with open(log_file, "a") as f:
            f.write(message)
