from flask import Blueprint, jsonify

bp = Blueprint("api", __name__)

@bp.route("/api/hello")
def hello():
    hello = "Hello, World!"
    first_api = "First Flask API"
    return jsonify(message=hello, first_api=first_api)

