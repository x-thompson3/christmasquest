from architecture.game import GameEngine

if __name__ == "__main__":
    game = GameEngine()

    while len(game.answer_dict) > 0:
        print(game.story_text)
        game.execute_actions()
        input_flag = True
        while input_flag:
            user_input = input("> ").upper()
            if game.check_answer(user_input) != "Incorrect Answer":
                input_flag = False
    print(game.story_text)