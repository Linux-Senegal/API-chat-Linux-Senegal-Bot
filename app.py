# coding=utf-8

import os
import sys
import aiml

from flask import Flask, request
from datetime import datetime
app = Flask(__name__)
 
# load the aiml file
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    #kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.learn("alice/*.aiml") 
    kernel.saveBrain("bot_brain.brn")

# set a constant
name = "LinuxSenegal"
kernel.setBotPredicate("name", name)
kernel.setBotPredicate("user", "user")

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello ;-)</h1>
    <p>It is currently {time}.</p>

    <img src="https://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/bot/', methods=['GET'])
def webhook():

    # endpoint for processing incoming messaging events
    sessionId = request.args.get("id")
    message = request.args.get("talk")
    kernel.setBotPredicate("user", request.args.get("user"))
    response = kernel.respond(message,sessionId)
    #log(response)  # you may not want to log every incoming message in production, but it's good for testing

    return response, 200


def log(message):  # simple wrapper for logging to stdout on heroku
    print (str(message))
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

