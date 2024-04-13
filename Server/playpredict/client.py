from flask import Blueprint, render_template
from . import game as g

client_bp = Blueprint("client", __name__)

g.initGame()

def updatePlay():
    pass

@client_bp.route("/")
def index():

    play_table_data = []
    for playnum in range(0, 4):
        a = dict()
        a['number'] = playnum

        play_table_data.append(a)

    prediction_table_data = []
    for prediction in range(0, 4):
        a = dict()
        a["rank"] = prediction
        a["play"] = "test"
        a["formation"] = "test"

        prediction_table_data.append(a)

    stat_table_data = []
    for stat in range(0, 4):
        a = dict()
        a["name"] = "test"
        a["value"] = "test"

        stat_table_data.append(a)

    return render_template("dashboard.html", plays=play_table_data, predictions=prediction_table_data, stats=stat_table_data)
