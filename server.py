from flask import Flask, request, render_template
import os
import tweepy

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

app = Flask(__name__)

app.secret_key = "SecretKey!"

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)


@app.route('/')
def homepage():
    """Display homepage"""

    return render_template('homepage.html')


@app.route('/results')
def search_twitter():
    """Receive search terms from js, send to twitter api to retrieve results"""

    original_search_terms = request.args.get('search-terms')
    tweet_filter = request.args.get('filter')
    number_of_tweets = request.args.get('number-of-tweets')
    language = request.args.get('language')

    if tweet_filter:
        search_terms = '%s filter:%s' % (original_search_terms, tweet_filter)
    else:
        search_terms = original_search_terms

    tweet_search = api.search(q=search_terms, lang=language, count=number_of_tweets, show_user=True)

    hashtags = {}

    for tweet in tweet_search:
        tweet = tweet.text.split()
        for word in tweet:
            if word[0] == '#':
                if word in hashtags:
                    hashtags[word] += 1
                else:
                    hashtags[word] = 1

    return render_template('results.html',
                           tweet_search=tweet_search,
                           hashtags=hashtags,
                           search_terms=original_search_terms)

if __name__ == "__main__":
    app.debug = True

    context = ('server-files/yourserver.crt', 'server-files/yourserver.key')
    app.run(ssl_context=context)
