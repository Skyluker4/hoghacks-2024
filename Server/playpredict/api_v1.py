from flask import (
    Blueprint, render_template, jsonify
)

api_v1_bp = Blueprint('api_v1', __name__,)


@api_v1_bp.route("/formations", methods=["GET"])
def get_formations():
    # Logic to retrieve formations
    formations = ['4-4-2', '4-3-3', '3-5-2']
    return jsonify(formations)


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
