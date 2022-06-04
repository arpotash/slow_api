import json
from json import JSONDecodeError
from urllib import parse


class Request:

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)
        self.body = self._get_body(environ)

    def _get_headers(self, environ: dict) -> dict:
        """
        Get headers of the request
        :param environ: wsgi set of the data
        :return: set of the headers
        """
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value
        return headers

    def _get_query_params(self, environ: dict) -> dict:
        """
        Get query params of the request
        :param environ: wsgi set of the data
        :return: set of the query_params
        """
        query_string = environ.get('QUERY_STRING')
        query_params = parse.parse_qs(query_string)
        return {key: value[0] for key, value in query_params.items()}

    def _get_body(self, environ: dict):
        if environ["REQUEST_METHOD"] == "GET":
            return {}
        if environ["CONTENT_LENGTH"] == "0":
            raise ValueError("body haven't to be an empty")
        body = environ["wsgi.input"].read().decode("utf-8")
        try:
            body_params = json.loads(body)
        except JSONDecodeError as e:
            body_content = parse.parse_qs(body)
            body_params = {key: value[0] for key, value in body_content.items()}
        with open("response.json", 'w') as json_obj:
            json.dump(body_params, json_obj, indent=4)
        return body_params

