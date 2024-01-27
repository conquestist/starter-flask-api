from flask import Flask
import os
import bot
app = Flask(__name__)

@app.route('/')
def hello_world():
    schedule.every().hour.do(bot.job)
    while True:
        schedule.run_pending()
        time.sleep(900)
    return 'Hello, world!'
