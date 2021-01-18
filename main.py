import os
import tweepy
import tensorflow as tf
import random


def entry():
    # Characters that the tweet can start with
    starters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', '@']

    # Bad Words
    sensitive_topics = [
        "BLM",
        "&amp"
        "Black",
        "blm",
        "black",
        "hispanic",
        "muslim",
        "illegal",
        "immigrant",
        "migrant",
        "racis",
        "sexis",
        "scum", "SCUM", "Scum",
        "ANTIFA",
        "antifa", "Antifa", "ANTIFA",
        "criminal", "Criminal", "CRIMINAL",
        "Covid", "covid", "19"
        "virus", "Virus", "VIRUS",
        "gay", "Gay", "GAY"
    ]

    # Twitter Developer API Keys
    consumer_key = os.environ.get('TWITTER_API_KEY')
    consumer_secret = os.environ.get('TWITTER_API_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')

    # Load the Model in from ./one_step (the model we trained in Jupyter)
    one_step_reloaded = tf.saved_model.load('one_step')

    # Set the settings for the model
    states = None
    # Pick a random character from starters[] to be the beginning letter of the tweet.
    next_char = tf.constant([random.choice(starters)])
    result = [next_char]

    bad_tweet = True

    def generateTweet(next_char, states, one_step_reloaded, result):
        result = [next_char]
        # Maximum length the tweet can be is 280
        for n in range(279):
            next_char, states = one_step_reloaded.generate_one_step(
                next_char, states=states)
            result.append(next_char)

        # Store the result in var called tweet_text
        tweet_text = tf.strings.join(result)[0].numpy().decode("utf-8")

        # Cut the tweet at the last full stop after about 200 characters i guess
        tweet_text = tweet_text.split(".")
        tweet_text = tweet_text[:-1]
        tweet_text = "".join(tweet_text) 
        tweet_text = tweet_text + "!"

        print(tweet_text)

        return tweet_text

    while (bad_tweet == True):
        tweet_text = generateTweet(
            next_char, states, one_step_reloaded, result)
        for word in sensitive_topics:
            if (word in tweet_text):
                bad_tweet = True
                # Stop looking if bad word found.
                break
            else:
                bad_tweet = False

    # Start to write it to twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Post tweet
    api.update_status(tweet_text)


entry()