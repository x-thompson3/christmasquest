"""
This module will display a Terminal-like screen, "unlocking" files by moving them into the given destination directory
when the correct password is entered.
"""
import json
import os.path

DEFAULT_STORY = "christmas21"
BASE_PATH = os.path.expanduser("~")


class FileUnlocker:
    def __init__(self, story_dir="christmas21", index="start"):
        if not os.path.isdir(os.path.join(f"{BASE_PATH}", f"{story_dir}")):
            print(f"Story directory '{story_dir}' does not exist")
            self.story_dir = DEFAULT_STORY
        else:
            self.story_dir = story_dir

        self.story_json = json.loads("{}")
        self.index = index
        self.file_dictionary = {}

    def move_to_target_dir(self, subdir=""):
        """
        This function will copy the file from the source_directory to the target_directory. If the subdir param is
        specified, it will place it in the target_directory/subdirectory
        :param subdir:
        :return:
        """
        pass

    def check_password(self, password):
        """
        This function checks whether or not the given password is correct given the following parameters:
        * The password is correct for any file in the loaded list
        * The files present in the target_directory are a superset of the "prereq_files" for that file
        :param password: user input, all lowercase
        :return:
        """
        pass

    def prompt_loop(self):
        """
        This function runs a while loop of using prompt() to ask for passwords.
        Special commands include the following:
        * 'hint': display a hint based on
        * 'exit' or 'q': end the while loop
        :return:
        """
        user_input = ""

        while True:
            user_input = input("> ").lower()
            if user_input in ('exit', 'q'):
                break
            elif user_input == 'hint':
                # give_hint() ???
                pass
            else:
                self.check_password(password=user_input)
        print("Goodbye.")


if __name__ == '__main__':
    pass
