from flask import Flask, render_template
import sys

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("/index.html")


# Notion Widgets
@app.route('/pointer/')
def pointer():
    return render_template("/widget/pointer.html")

@app.route('/postbox/')
def postbox():
    return render_template("/postbox.html")