from flask import Flask

def create_app():
    app = Flask('PlayPredict')

    from . import client
    from . import api_v1
    app.register_blueprint(client.client_bp)
    app.register_blueprint(api_v1.api_v1_bp, url_prefix='/api/v1')

    return app
