from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
        Interacts with HTPP
    """
    @staticmethod
    def validate_and_create(http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # business rules
        print("I'm in a view")
        # returns HTTP
        return HttpResponse(status_code=200, body={"hello": "world"})
