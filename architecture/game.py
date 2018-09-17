class GameEngine:
    """Class for holding current game state and a log of the adventure"""
    def __init__(self, story_dir="christmas18"):
        # Holds 
        self.phase = 1
        self.story_dir = story_dir
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
            self.answer_set = lines[1].strip().split('|')
            self.story_result = lines[2].strip()
        return self.story_text

    def set_story(self, p, i):
        """Set the current story text to the given values, and assume the input is valid."""
        self.phase = p
        self.index = i

    def next_story(self):
        """Increment the current index. If the story_dir/phase/index isn't a file, increment phase and set index
        to 1."""
        pass

    def check_answer(self, answer_in):
        """Check that answer_in is within the answer_set, return "incorrect answer" or the answer_text"""
        if answer_in in self.answer_set:
            return self.story_result
        else:
            return "Incorrect Answer"

    def logit(self, message, public=False):
        """Log the results to the internal.log"""
        log_file = 'The_Story_Thus_Far.log' if public else 'internal.log'
        with open(log_file, "a") as f:
            f.write(message)
