import architecture.game as game


def test_get_story():
    g_obj = game.GameEngine(story_dir="sample_story")
    assert g_obj.get_current_story() == "Here's the text of riddle 1."


def test_answer_set_single():
    g_obj = game.GameEngine(story_dir="sample_story")
    assert g_obj.get_current_story() == "Here's the text of riddle 1."
    assert len(g_obj.answer_dict) == 1

# def test_choice_set():
#     g_obj = game.GameEngine(story_dir="sample_story")
#     g_obj.set_story(2, 1)
#     print(g_obj.answer_dict)
#     assert g_obj.get_current_story() == "Here's a choices question."
#     assert len(g_obj.answer_dict) == 3
#     assert g_obj.check_answer("choice 1") == "Here's the result of your choices!"
#
#
# def test_story_out_of_bounds():
#     g_obj = game.GameEngine(story_dir="sample_story")
#     try:
#         while True:
#             # print(g_obj.get_current_story())
#             g_obj.next_story()
#     except IOError as e:
#         if "run out of story files" not in str(e):
#             raise
#         else:
#             return
