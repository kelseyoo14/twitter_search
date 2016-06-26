from flask import Flask, request, render_template, session, flash
from flask import redirect as flaskredirect
import requests
import os
import json

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")


@app.route('/')
def homepage():
    "Display homepage"

    return render_template('homepage.html')


@app.route('/results')
def search_twitter():
    "Receive search terms from js, send to twitter api to retrieve results"

    search_terms = request.args.get('search-terms')

    # results = response from twitter api request with search terms

    return render_template('results.html',
                           search_terms=search_terms)



if __name__ == "__main__":
    app.debug = True

    # DEBUG = "NO_DEBUG" not in os.environ
    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
