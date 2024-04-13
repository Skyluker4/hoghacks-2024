from flask import Blueprint, jsonify, request
import time as t
from . import game as g

g.initGame()

api_v1_bp = Blueprint(
    "api_v1",
    __name__,
)

# This function gets an array of selectable formations by the current team
@api_v1_bp.route("/formations", methods=["GET"])
def get_formations():
    return g.game.jsonFormations()


# Predict what the next play will be by the other team, given your formation (optionally)
@api_v1_bp.route("/predictions", methods=["GET"])
def get_predictions():
    formation_name = request.args.get("formation")
    g.game.updateCurrentFormation(formation_name)

    return g.game.jsonPredictions()


@api_v1_bp.route("/situation", methods=["GET"])
def get_situation():
    # Logic to retrieve situation
    return g.game.situation.toJSON()


@api_v1_bp.route("/time", methods=["POST"])
def set_time():
    # The request body is the time
    time = t.strptime(request.json["time"], "%M:%S")
    quarter = int(request.json["quarter"])

    g.game.situation.time = time
    g.game.situation.quarter = quarter

    return "", 204

@api_v1_bp.route("/score", methods=["POST"])
def update_score():
    score = request.json["home_score"], request.json["away_score"]
    g.game.updateScore(score)
    return "", 204

@api_v1_bp.route("/possession", methods=["POST"])
def update_possession():
    is_possessing_team = request.json["is_possessing_team"]
    g.game.updatePossession(is_possessing_team)
    return "", 204

@api_v1_bp.route("/position", methods=["POST"])
def update_position():
    position = (
        request.json["distance"],
        request.json["down"],
        request.json["yard"],
    )
    g.game.updatePosition(position)
    return "", 204

@api_v1_bp.route("/reset", methods=["POST"])
def reset():
    g.game = g.Game("Bentonville West", "Bentonville", True)
    return "", 204
