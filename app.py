from flask import Flask
import os
import bot
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/pussy')
def pussy():
    return 'pussy'

@app.route('duc')
def duc():
    bot.job()
    return "got you bro"

