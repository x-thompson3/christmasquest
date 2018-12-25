import os.path
import ast


class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, story_dir="christmas18", index="start"):
        if not os.path.isdir(f"../{story_dir}"):
            print(f"Story directory '{story_dir}' does not exist")
            self.story_dir = "christmas18"
        else:
            self.story_dir = story_dir

        self.index = index

        self.answer_dict = {}
        self.story_text = "No Story Test Yet."
        self.get_current_story()

    def get_current_story(self):
        """
        Pull the current story text and answer into class variables
        :return:
        """
        filename = f"../{self.story_dir}/{self.index}.txt"
        with open(filename, 'r') as f:
            lines = f.read().split("==")
            self.story_text = lines[0].strip()
            self.answer_dict = ast.literal_eval(lines[1].strip())
        return self.story_text

    def set_story(self, i):
        """Set the current story text to the given values, and check the file is extant."""
        filename = f"../{self.story_dir}/{i}.txt"
        if os.path.isfile(filename):
            self.index = i
            self.get_current_story()

    def check_answer(self, answer_in):
        """Check that answer_in is within the answer_set, return "incorrect answer" or the answer_text"""
        if len(self.answer_dict) == 0:
            return ""
        for possible in self.answer_dict.keys():
            if possible in answer_in:
                self.set_story(self.answer_dict[possible])
                return self.get_current_story()
        else:
            return "Incorrect Answer"

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_file = 'The_Story_Thus_Far.log' if public else 'internal.log'
        with open(log_file, "a") as f:
            f.write(message)
            f.write('\n')


if __name__ == "__main__":
    ge = GameEngine()
    print(ge.get_current_story())
    print(ge.check_answer("any key should do"))
    print(ge.check_answer("didgeridoo kazoo"))
    print(ge.check_answer("middle door"))
