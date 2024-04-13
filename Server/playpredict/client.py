from flask import Blueprint, render_template

client_bp = Blueprint("client", __name__)


@client_bp.route("/")
def index():
    return render_template('dashboard.html')
