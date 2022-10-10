from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def survey():
    print('surveyyyy')