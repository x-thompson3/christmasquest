import ast
import os.path

DEFAULT_STORY = "christmas21"
BASE_PATH = os.path.expanduser("..")


class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, story_dir="christmas21", index="start"):
        if not os.path.isdir(f"{BASE_PATH}/{story_dir}"):
            print(f"Story directory '{story_dir}' does not exist")
            self.story_dir = DEFAULT_STORY
        else:
            self.story_dir = story_dir

        self.index = index
        self.story_text = "No Story Test Yet."
        self.answer_dict = {}
        self.action = None

    def get_current_story(self):
        """
        Pull the current story text and answer into class variables
        :return:
        """
        filename = os.path.join(os.path.join(f'{BASE_PATH}', f'{self.story_dir}'), f'{self.index}.txt')
        with open(filename, 'r') as f:
            lines = f.read().split("==")
            self.story_text = lines[0].strip()
            try:
                self.answer_dict = ast.literal_eval(lines[1].strip())
            except Exception as e:
                print(f"Something went wrong when reading answer_dictionary: {str(e)}")
                self.answer_dict = {}

            try:
                exec(lines[2].strip())
            except Exception as e:
                print(f"Something went wrong when reading action: {str(e)}")

        return self.story_text

    def set_story(self, i):
        """Set the current story text to the given values, and check the file is extant."""
        filename = os.path.join(os.path.join(f'{BASE_PATH}', f'{self.story_dir}'), f'{i}.txt')
        if os.path.isfile(filename):
            self.index = i
            return self.get_current_story()
        else:
            raise Exception(f"Error! {filename} is not a story file")

    def check_answer(self, answer_in):
        """Check that answer_in is within the answer_set, return "incorrect answer" or the answer_text"""
        if len(self.answer_dict) == 0:
            return ""
        for possible in self.answer_dict.keys():
            if possible in answer_in:
                return self.set_story(self.answer_dict[possible])
        else:
            return "Incorrect Answer"

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_name = 'The_Story_Thus_Far.log' if public else 'internal.log'
        filename = os.path.join(os.path.join(f'{BASE_PATH}', f'{self.story_dir}'), f'{log_name}.txt')
        with open(filename, "a") as f:
            f.write(message)
            f.write('\n')


if __name__ == "__main__":
    ge = GameEngine()
    print(ge.get_current_story())
    print(ge.check_answer("start"))
