from dataclasses import dataclass


@dataclass
class HttpRequest:
    header: dict | None = None
    body: dict | None = None
    query_params: dict | None = None
