from flask import Blueprint, jsonify
import time as t
from . import formation

api_v1_bp = Blueprint('api_v1', __name__,)

@api_v1_bp.route("/formations", methods=["GET"])
def get_formations():
    return Response(g.game.jsonFormations(), mimetype='application/json')


# Predict what the next play will be by the other team, given your formation (optionally)
@api_v1_bp.route("/predictions", methods=["GET"])
def get_predictions():
    formation_name = request.args.get("formation")

    if formation_name:
        g.game.updateCurrentFormation(formation_name)
    g.game.predict()

    return Response(g.game.jsonPredictions(), mimetype='application/json')


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
