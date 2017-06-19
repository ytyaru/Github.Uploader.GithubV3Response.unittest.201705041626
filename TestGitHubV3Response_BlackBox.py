import unittest
from web.service.github.api.v3.Response import Response
import requests
class TestGitHubV3Response_BlackBox(unittest.TestCase):
    def test_Get_Json(self):
        url = 'https://api.github.com/users'
        kwargs = {'headers': {'Time-Zone': 'Asia/Tokyo', 'Accept': 'application/vnd.github.v3+json', 'User-Agent': ''}}
        r = requests.get(url, **kwargs)
        res = Response().Get(r)
        self.assertEqual(list, type(res))
        self.assertEqual(dict, type(res[0]))
    # application/vnd.github.*.rawについて単体試験しない。rawが返るAPIについて知らないし使う予定もないため。
    # Content-TypeがNoneになることはない。例外が発生する。Exception: MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。入力値: 

