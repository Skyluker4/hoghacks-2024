from flask import Blueprint, render_template
from . import game as g

client_bp = Blueprint("client", __name__)

g.initGame()

def updatePlay():
    pass

@client_bp.route("/")
def index():
    return render_template("dashboard.html")
