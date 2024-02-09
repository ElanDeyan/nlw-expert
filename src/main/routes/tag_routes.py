from flask import Blueprint, Response, request, jsonify
from src.errors.errors_handler import errors_handler
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags() -> tuple[Response, int]:
    print(request.json)

    response: HttpResponse

    try:
        http_request = HttpRequest(body=request.json)
        response = TagCreatorView.validate_and_create(http_request)
    except Exception as exception:
        response = errors_handler(exception)

    return jsonify(response.body), response.status_code
