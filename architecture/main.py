from architecture.twitter import TwitterBot
from architecture.game import GameEngine

if __name__ == "__main__":
    birdy = TwitterBot()
    story = GameEngine()

    story.logit("The Christmas Quest begins!")
    birdy.send_tweet("He's done it!")
