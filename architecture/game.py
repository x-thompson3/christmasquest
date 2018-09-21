import os.path


class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, story_dir="christmas18"):
        if not os.path.isdir(f"../{story_dir}"):
            print(f"Story directory '{story_dir}' does not exist")
            self.story_dir = "christmas18"
        else:
            self.story_dir = story_dir

        self.phase = 1
        self.index = 1

        self.answer_set = {}
        self.story_text = "No Story Test Yet."
        self.story_result = "No Story Result Yet."

    def get_current_story(self):
        """
        Pull the current story text and answer into class variables
        :return:
        """
        filename = f"../{self.story_dir}/{self.phase}/{self.index}.txt"
        with open(filename, 'r') as f:
            lines = f.read().split("==")
            self.story_text = lines[0].strip()
            self.answer_set = [x.lower().strip() for x in lines[1].split('|')]
            self.story_result = lines[2].strip()
        return self.story_text

    def set_story(self, p, i):
        """Set the current story text to the given values, and assume the input is valid."""
        filename = f"../{self.story_dir}/{p}/{i}.txt"
        if os.path.isfile(filename):
            self.phase = p
            self.index = i
            self.get_current_story()

    def next_story(self):
        """Increment the current index. If the story_dir/phase/index isn't a file, increment phase and set index
        to 1."""
        self.index += 1
        filename = f"../{self.story_dir}/{self.phase}/{self.index}.txt"
        if not os.path.isfile(filename):
            self.set_story(self.phase+1, 1)
            filename = f"../{self.story_dir}/{self.phase}/{self.index}.txt"
            if not os.path.isfile(filename):
                raise IOError(f"You've run out of story files at p={self.phase}, i={self.index}!")
        self.get_current_story()

    def check_answer(self, answer_in):
        """Check that answer_in is within the answer_set, return "incorrect answer" or the answer_text"""
        if answer_in.lower() in self.answer_set:
            return self.story_result
        else:
            return "Incorrect Answer"

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_file = 'The_Story_Thus_Far.log' if public else 'internal.log'
        with open(log_file, "a") as f:
            f.write(message)
            f.write('\n')
