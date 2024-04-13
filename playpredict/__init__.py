from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import page
    app.register_blueprint(page.bp)

    return app
