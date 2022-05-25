from slow_api.response import Response
from slow_api.url import Url
from slow_api.wsgi import SlowApi
from slow_api.view import BasedView


class MyFirstView(BasedView):

    def post(self, request):
        return Response(status=201, json='Hello, post', headers={'Babayka': '123'})

    def get(self, request):
        return Response(json='Hello, get', headers={'Babayka': '132'})


urls = [
    Url('/homepage/page/<str:name>', MyFirstView),
]

app = SlowApi(urls)


