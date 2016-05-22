# -*- coding: utf-8 -*-
import os
from datetime import datetime, date
from requests import get, ConnectionError
from flask import Flask, render_template, send_from_directory
from simplejson.decoder import JSONDecodeError

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

try:
    sl_api_key_realtime_dep = os.environ['SL_API_KEY_REALTIMEDEP']
except KeyError:
    sl_api_key_realtime_dep = None

@app.route('/')
def index():
    if sl_api_key_realtime_dep:
        error = None
        mids_next = []
        
        try:
            mids = get("https://api.sl.se/api2/realtimedepartures.json?key=" + sl_api_key_realtime_dep +
                        "&siteid=9264&timewindow=30").json()
        except JSONDecodeError:
            print("No data fetched for midsommarkransen")
            mids = None
        except ConnectionError:
            error = "Can't connect to SL server for fetching latest data"
            print(error)
        else:
            print mids
            if mids and mids.get(u'ResponseData', None):
                for metro in mids.get(u'ResponseData', None).get(u'Metros', None):
                    if metro.get(u'JourneyDirection', None) == 1:
                        print(metro)
                        mids_next.append(metro.get(u'DisplayTime', None))

        return render_template('index.html',
                               error=error,
                               mids_next=mids_next,
                              )
    return render_template('index.html', error="Trafiklab API Key not defined. Please add it as an env variable.")

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
