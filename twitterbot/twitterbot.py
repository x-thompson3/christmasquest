import tweepy

def main():
    CONSUMER_KEY = 'replace with your key'
    CONSUMER_SECRET = 'replace with your secret'
    ACCESS_KEY = 'replace with your access key'
    ACCESS_SECRET = 'replace with your access secret'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status("Sending my first tweet via Tweepy!")

def read_from_secret(fname):
    ret = ""
    with open("../secret/"+fname) as f:
        ret = f.readlines()
        
