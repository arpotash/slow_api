from slow_api.response import Response


class BasedView:

    def get(self, request, *args, **kwargs) -> Response:
        pass

    def post(self, request, *args, **kwargs) -> Response:
        pass
