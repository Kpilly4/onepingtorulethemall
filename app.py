from flask import Flask, render_template, request
import requests
import time


app = Flask(__name__)


@app.route('/')
def home():
    panels = [
        {"title": "Analog'Digtal", "url": "https://www.analogdigital.ca"},
        {"title": "ShiftConnect", "url": "https://www.shiftconnect.com"},
        {"title": "OneTwoPay", "url": "https://www.onetwopay.ca"},
        {"title": "PayFromAway", "url": "https://www.payfromaway.ca"},
        {"title": "Debbie Pushor", "url": "https://www.debbiepushor.ca"},
        {"title": "Canmore Folk Music Festival", "url": "https://www.canmorefolkfestival.com"},
        {"title": "Bowda", "url": "https://www.bowda.ca"},
        {"title": "De Lumber", "url": "https://www.delumber.com"},
        {"title": "MindYrLife", "url": "https://www.mindyrlife.com"},
        {"title": "Brewster's Mountain lodge", "url": "https://www.brewstermountainlodge.com"},
        {"title": "The Edge Exotic", "url": "https://www.theedgeexotic.com"},


    ]
    return render_template("home.html", panels=panels)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/ping")
def ping():
    url = request.args.get("url")
    start_time = time.time()
    r = requests.get(url)
    end_time = time.time()

    diff_time = int((end_time - start_time) * 1000)

    return {"url": url,
            "code": r.status_code,
            "speed": diff_time
            }
