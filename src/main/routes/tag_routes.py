from flask import Blueprint, Response, request, jsonify

tags_routes_bp = Blueprint("tags_routes", __name__)

@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags() -> tuple[Response, int]:
    print(request.json)

    return jsonify({ "response": "ok" }), 200
