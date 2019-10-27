import json

__all__ = ["Response"]


class Response:
    """The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.

    :param status_code: response status code
    :param text: response content
    :param headers: response headers
    :param url: request url
    """

    def __init__(self, status_code: int, text: str, headers: dict, url: str) -> None:
        self.status_code = status_code
        self.text = text
        self.headers = headers
        self.url = url

    def json(self) -> dict:
        """convert the content to dict

        :return: the content from server
        """
        return json.loads(self.text)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented  # pragma: no cover
        return (
            self.status_code == other.status_code
            and self.text == other.text
            and self.headers == other.headers
            and self.url == other.url
        )

    def __str__(self):
        return "<Response [%s]>" % self.status_code
