# donaldgenerated
An A.I. Twitter Bot that posts trump-like tweets every hour.

## Where to view the Account
https://twitter.com/donaldgenerated

## How it's made
This was made using Tensorflow's Text Generation Model
https://www.tensorflow.org/tutorials/text/text_generation 

The model was fed all of Donald Trump's tweets available here: https://www.thetrumparchive.com/faq

The model posts once an hour after a few checks to try my best to ensure the content the bot posts is kept funny and not offensive.

The bot runs on Google Cloud Schedule; where a CRON job controls a Google Cloud Function executing the python code; in `entry()` in `main.py`
The CRON job is triggered every hour, on the hour.
