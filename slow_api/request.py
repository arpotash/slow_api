from urllib import parse


class Request:

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)

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
