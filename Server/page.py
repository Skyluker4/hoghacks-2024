import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('hello', __name__)

@bp.route('/hello')
def hello():
    return render_template('index.html')