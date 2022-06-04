import re
from dataclasses import dataclass
from slow_api.view import BasedView


@dataclass
class Url:
    path: str
    view: BasedView


class UrlMatcher:

    def __init__(self, url):
        self.url = url

    def _get_match_url(self, path: str) -> bool:
        """
        Convert and get url pattern and compare with url from client
        :param path: client's input url
        :return: is there match input url and pattern or not
        """
        pattern = self._convert_url()
        return bool(re.search(pattern, path))

    def _convert_url(self) -> str:
        """
        Function takes url and returns pattern for matching
        If there is path in this form <int:num>, gets type of the path
        and put match regex
        :return full pattern for matching with url
        """
        url_path = self.url.path.split('/')
        pattern_elem_lst = []
        for path in url_path:
            pattern_path = path
            if path.startswith("<") and path.endswith(">"):
                path_type_math = re.search(":", path)
                if path_type_math:
                    path_type = path[1:path_type_math.start()]
                    pattern_path = r"\d+" if path_type == "int" else r"\w+"
            pattern_elem_lst.append(pattern_path)
        return str.join('/', pattern_elem_lst)
