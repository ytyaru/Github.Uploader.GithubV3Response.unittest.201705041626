import unittest
#from AuthenticationsCreator import AuthenticationsCreator
#from web.service.github.api.v3.AuthenticationsCreator import AuthenticationsCreator
#from web.service.github.api.v3.RequestParameter import RequestParameter
from web.service.github.api.v3.Response import Response
class TestGitHubV3Response_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(Response, 'Get'))
        
