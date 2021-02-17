from flask import Flask, render_template
import sys

from logging.handlers import RotatingFileHandler
import logging

logging.basicConfig(filename = "server.log", level = logging.INFO)
application=Flask(__name__)

app = Flask(__name__)

@app.route('/')
def jsLab01():
    return render_template("/jsLab01.html")

@app.route('')
def 
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)