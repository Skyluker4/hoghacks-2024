from flask import Blueprint, jsonify
import time as t
from . import formation

api_v1_bp = Blueprint('api_v1', __name__,)

@api_v1_bp.route("/formations", methods=["GET"])
def get_formations():
    # Logic to retrieve formations
    current_formation = formation.Formation('Doubles')
    return current_formation.toJSON()


@api_v1_bp.route("/prediction", methods=["GET"])
def get_prediction():
    # Logic to retrieve prediction
    prediction = 'Team A will win'
    return jsonify(prediction)


@api_v1_bp.route("/situation", methods=["GET"])
def get_situation():
	# Logic to retrieve situation
	situation = 'Team B is leading 2-1'
	return jsonify(situation)


@api_v1_bp.route("/time", methods=["POST"])
def set_time():
    # The request body is the time
    time = t.strptime(request.json['time'], "%M:%S")
    quarter = int(request.json['quarter'])
    return "", 204
