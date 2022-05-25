from typing import Union, Any

from slow_api.request import Request
from slow_api.view import BasedView
from slow_api.url import UrlMatcher


class SlowApi:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        if bool(response):
            start_response(str(response.status), list(response.headers.items()))
            return [response.json.encode()]

    def _get_view(self, request: Request) -> Union[BasedView, None]:
        """
        Get path from request, match check and get view function for this url if there is
        :param request: request params
        :return: view function for the url or None if not match
        """
        path = request.path
        for url in self.urls:
            url_matcher = UrlMatcher(url)
            is_url_match = url_matcher._get_match_url(path)
            if is_url_match:
                return url.view
            return None

    def _get_response(self, request: Request, view: BasedView) -> Any:
        """
        Call view for the url and get response
        :param request: request params
        :param view: url view function
        :return: response as a result of the view
        """
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return "Метод не поддерживается"
