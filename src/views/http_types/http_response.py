from dataclasses import dataclass


@dataclass
class HttpResponse:
    status_code: int
    body: dict
