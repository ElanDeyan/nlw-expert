from src.views.http_types.http_response import HttpResponse


def errors_handler(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500, body={"errors": [{"title": "Server error", "detail": str(error)}]}
    )
