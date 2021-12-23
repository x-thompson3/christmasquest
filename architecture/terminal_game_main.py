from game import GameEngine

if __name__ == "__main__":
    game = GameEngine()

    while len(game.answer_dict) > 0:
        print()
        print(game.story_text)
        print()
        game.execute_actions()
        input_flag = True
        while input_flag:
            user_input = input("> ").lower()
            if game.check_answer(user_input) != "Incorrect Answer":
                input_flag = False
            elif "hint" in user_input.lower():
                print("TODO: Complete Hint List")
            elif "help" in user_input.lower():
                print("No.")
    print()
    print(game.story_text)