from flask import Flask, g, Response, make_response, request
from flask import session, render_template, Markup
from datetime import date, datetime, timedelta
from flaskapp.modules.statData import statSearch
from flaskapp.modules.getKey import getKey

app = Flask(__name__)
app.debug = True


@app.route("/")
def main(value=None):
    return render_template('main.html')


@app.route("/stat", methods=['GET'])
def post(value=None):
    key = getKey()
    value = request.args.get('statSearch')
    region = 'kr'
    stat = statSearch(key, region, value)

    return render_template('stat.html.j2', stat=stat)
