import tweepy
import game


class TwitterBot(tweepy.StreamListener):
    """Class for managing twitter API calls and responses.
    It holds a GameEngine object which will handle checking answers to riddles and """

    def __init__(self, game_engine):
        super().__init__()
        CONSUMER_KEY = self.read_from_secret('consumer_key')
        CONSUMER_SECRET = self.read_from_secret('consumer_secret')
        ACCESS_KEY = self.read_from_secret('access_key')
        ACCESS_SECRET = self.read_from_secret('access_secret')

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.name = self.read_from_secret('name')
        self.api = tweepy.API(auth)
        self.game_engine = game_engine

    def read_from_secret(self, fname):
        ret = ""
        with open("../secret/" + fname + ".txt") as f:
            lines = f.readlines()
            assert len(lines) == 1, f"{fname} has more than one line in it!"
            ret = lines[0].strip()
        assert ret != "", f"{fname} failed to load"
        return ret

    def send_tweet(self, tweet_text):
        """
        Basic functionality to send out tweet
        :return:
        """
        self.api.update_status(tweet_text)

    def respond_to_ans(self, message):
        """
        Called when someone tweets at the bot with a "!ans"
        :return:
        """
        print(f"\tReceived answer: '{message}'")
        pass

    def respond_to_choice(self, message):
        """
        Called when someone tweets at the bot with a "!choice"
        :return:
        """
        print(f"\tReceived choice: '{message}'")
        pass

    def start_listening(self):
        """
        Begin listening to Twitter stream for activation phrase.
        :return:
        """
        my_stream = tweepy.Stream(auth=self.api.auth, listener=self)
        print(f'Listening for self.name = {self.name}')
        my_stream.filter(track=[self.name])

    def on_status(self, status):
        if 'ans' in status.text:
            self.respond_to_choice(status.text)
        elif 'choice' in status.text:
            self.respond_to_choice(status.text)
        elif 'kill' in status.text:
            self.send_tweet("Bot was successfully switched off.")
            return False
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
        print(status_code)
        self.send_tweet("It's not working :(")

    def begin(self):
        pass
