import architecture.game as game


def test_get_story():
    g_obj = game.GameEngine()
    g_obj.set_story(1, 0)
    assert g_obj.get_current_story() == "Here's some story text"
    assert g_obj.check_answer("bad answer") == "Incorrect Answer"
    assert g_obj.check_answer("sample answer") == "Test Result message"
