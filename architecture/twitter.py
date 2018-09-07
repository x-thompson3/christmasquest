import tweepy


class TwitterBot:
    """Class for managing twitter API calls and responses"""
    def __init__(self):
        CONSUMER_KEY = self.read_from_secret('consumer_key')
        CONSUMER_SECRET = self.read_from_secret('consumer_secret')
        ACCESS_KEY = self.read_from_secret('access_key')
        ACCESS_SECRET = self.read_from_secret('access_secret')

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def read_from_secret(self, fname):
        ret = ""
        with open("../secret/"+fname+".txt") as f:
            lines = f.readlines()
            assert len(lines) == 1, f"{fname} has more than one line in it!"
            ret = lines[0]
        assert ret != "", f"{fname} failed to load"
        return ret

    def send_tweet(self, tweet_text):
        """
        Basic functionality to send out tweet
        :return:
        """
        self.api.update_status(tweet_text)

    def respond_to_ans(self):
        """
        Called when someone tweets at the bot with a "!ans"
        :return:
        """
        pass

    def respond_to_choice(self):
        """
        Called when someone tweets at the bot with a "!choice"
        :return:
        """
        pass


class MyStreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
