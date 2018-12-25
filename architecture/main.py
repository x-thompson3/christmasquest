from architecture.twitter import TwitterBot
from architecture.game import GameEngine

if __name__ == "__main__":
    story = GameEngine(story_dir="sample_story")
    birdy = TwitterBot(story)

    birdy.start_listening()
