import json
import os.path

import file_utils

DEFAULT_STORY = "christmas21"
BASE_PATH = os.path.join(os.path.expanduser("~"), "Documents")
# BASE_PATH = os.path.expanduser("..")


class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, source_path=BASE_PATH, story_dir="christmas21", index="start"):
        full_path = os.path.join(f"{source_path}", f"{story_dir}")
        if not os.path.isdir(full_path):
            raise NotADirectoryError(f"Story directory '{full_path}' does not exist")
        else:
            self.story_dir = full_path

        self.story_json = json.loads("{}")
        self.index = index
        self.story_text = "No Story Test Yet."
        self.answer_dict = {}
        self.action_list = []
        self.read_story_from_index()

    def read_story_from_index(self):
        """Pull the current story information into class variables"""
        filename = os.path.join(f'{self.story_dir}', f'{self.index}.json')
        with open(filename, 'r') as f:
            self.story_json = json.load(f)
            self.story_text = "\n".join(self.story_json['story_text'])
            self.answer_dict = self.story_json['answer_dict']
            self.action_list = self.story_json['action_list']
        return self.story_text

    def execute_actions(self):
        """Execute the list of actions in order"""
        for command_str in self.action_list:
            try:
                exec(command_str.strip())
            except Exception as e:
                print(f"Something went wrong when reading action ({command_str}): {str(e)}")

    def set_story(self, i):
        """Set the current story text to the given values, and check the file is extant."""
        filename = os.path.join(f'{self.story_dir}', f'{i}.json')
        if os.path.isfile(filename):
            self.index = i
            return self.read_story_from_index()
        else:
            raise Exception(f"Error! {filename} is not a story file")

    def check_answer(self, answer_in):
        """Check that answer_in is within the answer_set, return "incorrect answer" or the answer_text"""
        if len(self.answer_dict) == 0:
            return ""
        if '<any>' in self.answer_dict.keys():
            return self.set_story(self.answer_dict["<any>"])
        for possible in self.answer_dict.keys():
            if possible.lower() in answer_in.lower():
                return self.set_story(self.answer_dict[possible.lower()])
        else:
            return "Incorrect Answer"

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_name = 'The_Story_Thus_Far.log' if public else 'internal.log'
        filename = os.path.join(f'{self.story_dir}', f'{log_name}.txt')
        with open(filename, "a") as f:
            f.write(message)
            f.write('\n')


if __name__ == "__main__":
    ge = GameEngine()
    ge.read_story_from_index()
    print(ge.story_text)
    ge.execute_actions()
    ge.check_answer("start")
    print(ge.story_text)

