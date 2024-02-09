from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
    Interacts with HTPP
    """

    @staticmethod
    def validate_and_create(http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        if "product_code" in body:
            product_code: str = str(body["product_code"])
            formatted_response = TagCreatorController().create(product_code)
            return HttpResponse(status_code=200, body=formatted_response)

        return HttpResponse(
            status_code=401,
            body={
                "request_error": {
                    "cause": "'product_code' key not found in request's body"
                }
            },
        )
