from flask import Blueprint, render_template, request, redirect
from . import game as g
from . import formation as f
from . import situation as s
from . import play as p
from . import position as pos

client_bp = Blueprint("client", __name__)

g.initGame()


def updatePlay():
    pass


@client_bp.route("/")
def index():

    play_table_data = []
    i = 1
    for play in g.game.previous_plays_and_situations:
        a = dict()
        a["number"] = i
        i = i + 1

        play_table_data.append(a)

    prediction_table_data = []
    i = 1
    for prediction in g.game.predictions:
        a = dict()
        a["rank"] = i
        i = i + 1
        a["play"] = prediction.name
        a["formation"] = prediction.formation

        prediction_table_data.append(a)

    stat_table_data = []
    stat_table_data.append(
        {"name": "Away Score", "value": f"{g.game.situation.away_score}"}
    )
    stat_table_data.append(
        {"name": "Home Score", "value": f"{g.game.situation.home_score}"}
    )
    stat_table_data.append({"name": "Quarter", "value": f"{g.game.situation.quarter}"})
    stat_table_data.append({"name": "Time", "value": f"{g.game.situation.time}"})
    stat_table_data.append(
        {"name": "Down", "value": f"{g.game.situation.position.down}"}
    )
    stat_table_data.append(
        {"name": "Distance", "value": f"{g.game.situation.position.distance}"}
    )
    stat_table_data.append(
        {"name": "Position", "value": f"{g.game.situation.position.yard}"}
    )

    # f.defense_formations, string
    own_formations_data = []
    for formation in f.defense_formations:
        own_formations_data.append(formation.name)

    # f.offense_formations, string
    their_formations_data = []
    for formation in f.offense_formations:
        their_formations_data.append(formation.name)


    # p.offense_plays, number and name
    plays_avail_data = []
    # iterate through this list with i index
    for i, play in enumerate(p.offense_plays):
        a = dict()
        a["number"] = i
        a["name"] = play.name
        plays_avail_data.append(a)

    return render_template(
        "dashboard.html",
        plays=play_table_data,
        predictions=prediction_table_data,
        stats=stat_table_data,
        show_video=False,
        own_formations=own_formations_data,
        their_formations=their_formations_data,
        plays_avail=plays_avail_data,
    )


# Route number to play number /#
@client_bp.route("/<int:playnum>")
def play(playnum):
    play_table_data = []
    i = 1
    for play in g.game.previous_plays_and_situations:
        a = dict()
        a["number"] = i
        i = i + 1

        play_table_data.append(a)

    prediction_table_data = []
    i = 1
    for prediction in g.game.predictions:
        a = dict()
        a["rank"] = i
        i = i + 1
        a["play"] = prediction.name
        a["formation"] = prediction.formation

        prediction_table_data.append(a)

    stat_table_data = []
    stat_table_data.append(
        {"name": "Away Score", "value": f"{g.game.situation.away_score}"}
    )
    stat_table_data.append(
        {"name": "Home Score", "value": f"{g.game.situation.home_score}"}
    )
    stat_table_data.append({"name": "Quarter", "value": f"{g.game.situation.quarter}"})
    stat_table_data.append({"name": "Time", "value": f"{g.game.situation.time}"})
    stat_table_data.append(
        {"name": "Down", "value": f"{g.game.situation.position.down}"}
    )
    stat_table_data.append(
        {"name": "Distance", "value": f"{g.game.situation.position.distance}"}
    )
    stat_table_data.append(
        {"name": "Position", "value": f"{g.game.situation.position.yard}"}
    )

    return render_template(
        "dashboard.html",
        plays=play_table_data,
        predictions=prediction_table_data,
        stats=stat_table_data,
        video_url=f"/static/videos/{playnum + 1}.mp4",
        show_video=True,
    )


@client_bp.route("/handle_predict", methods=["POST"])
def handle_predict():
    print(str(request.form))
    #their_formation = request.form["theirformation"]
    #g.game.other_formation = f.Formation(their_formation)
    #g.game.predict()
    return redirect("/")


@client_bp.route("/handle_new_play", methods=["POST"])
def handle_new_play():
    their_formation = request.form["their_formation"]
    own_formation = request.form["own_formation"]
    play = request.form["play"]
    down = request.form["down"]
    position = request.form["position"]
    distance = request.form["distance"]

    g.game.other_formation = f.Formation(their_formation)
    g.game.current_formation = f.Formation(own_formation)
    g.game.situation.position = pos.Position(position, down, distance)
    g.game.previous_plays_and_situations.append((play, g.game.situation))

    g.game.predict()

    return redirect("/")
