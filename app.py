from flask import Flask, render_template
import sys

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("/index.html")


# mdforest
## pointer
@app.route('/pointer/')
def pointer():
    return render_template("/widget/pointer.html")

## postbox
@app.route('/postbox/')
def postbox():
    return render_template("/postbox.html")

## atm
@app.route('/atm/')
def atm():
    return render_template("/atm/atm.html")

@app.route('/pay/')
def pay():
    return render_template("/atm/pay.html")