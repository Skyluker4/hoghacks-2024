from flask import Blueprint, jsonify, request
import time as t
from . import game as g

api_v1_bp = Blueprint('api_v1', __name__,)

game = g.Game("Bentonville West", "Bentonville", True)

# This function gets an array of selectable formations by the current team
@api_v1_bp.route("/formations", methods=["GET"])
def get_formations():
	global game
	# Return an array of Formations with their suggested weights
	return jsonify(game.formations)


# Predict what the next play will be by the other team
@api_v1_bp.route("/predictions", methods=["GET"])
def get_predictions():
	global game
	# Logic to retrieve prediction
	return game.predictions


@api_v1_bp.route("/situation", methods=["GET"])
def get_situation():
	# Logic to retrieve situation
	global game
	return game.situation.toJSON()


@api_v1_bp.route("/time", methods=["POST"])
def set_time():
	global game
	# The request body is the time
	time = t.strptime(request.json['time'], "%M:%S")
	quarter = int(request.json['quarter'])

	game.situation.time = time
	game.situation.quarter = quarter

	return "", 204

@api_v1_bp.route("/reset", methods=["POST"])
def reset():
	global game
	game = g.Game("Bentonville West", "Bentonville", True)
	return "", 204
