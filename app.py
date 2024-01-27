from flask import Flask
import os
import bot
app = Flask(__name__)

@app.route('/')
def hello_world():
    bot.job()
    return 'Hello, world!'
