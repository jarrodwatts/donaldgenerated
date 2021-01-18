import json

sensitive_topics = [
    "BLM",
    "Black",
    "blm",
    "black",
]

with open('./trump_tweet_data/tweets.json', encoding="utf8") as f:
    data = json.load(f)

for tweet in data:
  try:
    # Perform filtering of tweets

    # 0. remove retweets
    # If the tweet.isRetweet == f
    if (tweet["isRetweet"] == 'f'):
        # 1. remove image tweets
        if ("t.co/" not in tweet["text"]):
            # Filter out sensitive topics
            if (any(ele not in tweet["text"] for ele in sensitive_topics)):
                print(tweet["text"])

                # Write to file:
                f = open("output.txt", "a")
                f.write(tweet["text"])
                f.write('\n')
                f.write('\n')
                f.close()

  except:
    continue

# print(tweet["text"])