class Response:

    def __init__(self, json=None, status=200, headers=None, body=None):
        self.status = status
        self.headers = headers
        self.json = json
        self.body = body

    @staticmethod
    def _set_headers(user_headers: dict) -> dict:
        """
        Update current headers if there are any headers from client side
        :param user_headers: headers from client side
        :return: updated headers
        """
        headers = {
            'Content-Type': 'text/html'
        }

        if user_headers:
            headers.update(user_headers)
        return headers
