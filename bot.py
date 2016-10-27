import os
import time
from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
# Make your bot read the book!
tweetbot.read(book)

my_first_text = tweetbot.generate_text()
print("tweetbot says:")
print(my_first_text)


# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = ""
# Consumer Secret (API Secret)
cons_secret = ""
# Access Token
access_token = ""
# Access Token Secret
access_token_secret = ""

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)



# Set some parameters for your bot
targetstring = 'khe berga'
keywords = ['khe berga', 'kheberga']
prefix = 'when'
suffix = '#kheberga'
maxconvdepth = 2

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, keywords=None, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
# tweetbot.twitter_autoreply_stop()

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=5, keywords=None, prefix=None, suffix=suffix)

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
# tweetbot.twitter_tweeting_stop()

# DO SOMETHING HERE TO ALLOW YOUR BOT TO BE ACTIVE IN THE BACKGROUND
# You could, for example, wait for a week:
secsinday = 24 * 60 * 60
time.sleep(secsinday)
 
# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
tweetbot.twitter_autoreply_stop()

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
tweetbot.twitter_tweeting_stop()