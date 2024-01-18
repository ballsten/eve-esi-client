import unittest
from unittest.mock import MagicMock, Mock

from urllib.parse import urlparse, parse_qs

from esi_client.api_security import ApiSecurity

class TestSecurityApi(unittest.TestCase):
    """SearchApi unit test stubs"""
    def setUp(self) -> None:
        self.client_id = 'testClientId'
        self.callback_uri = 'http://localhost:45623/auth/callbak'
        self.api_security = ApiSecurity(self.client_id, self.callback_uri)

    def tearDown(self) -> None:
        pass
    
    ### test cases for _get_auth_uri
    
    # url
    def test_generate_uri_correct_host(self) -> None:  
        uri = self.api_security._get_auth_uri([])
        parsed_uri = urlparse(uri)
        
        self.assertEqual(parsed_uri.scheme, 'https')
        self.assertEqual(parsed_uri.netloc, 'login.eveonline.com')
        self.assertEqual(parsed_uri.path, '/v2/oauth/authorize')
    
    # redirect_uri
    def test_generate_uri_correct_redirect_uri(self) -> None:        
        scopes = []
        
        uri = self.api_security._get_auth_uri(scopes)
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('redirect_uri', qs.keys())
        self.assertEqual(self.callback_uri, qs['redirect_uri'][0])
    
    # scopes    
    def test_generate_uri_with_no_scopes(self) -> None:        
        scopes = []
        
        uri = self.api_security._get_auth_uri(scopes)
        qs = parse_qs(urlparse(uri).query)
        
        self.assertNotIn('scope', qs.keys())
    
    def test_generate_uri_with_one_scope(self) -> None:        
        scopes = ['test-scope']
        
        uri = self.api_security._get_auth_uri(scopes)
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('scope', qs.keys())
        self.assertEqual(scopes[0], qs['scope'][0])
    
    def test_generate_uri_with_multiple_scopes(self) -> None:
        """
        Multiple scopes are joined into one string seperated by a space
        """   
        scopes = ['test-scope-1', 'test-scope-2']
        
        uri = self.api_security._get_auth_uri(scopes)
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('scope', qs.keys())
        self.assertEqual(' '.join(scopes), qs['scope'][0])
    
    # state
    def test_generate_url_uses_unique_state(self) -> None:
        state = "test-state"
        
        self.api_security._generate_state = Mock(return_value=state)
        
        uri = self.api_security._get_auth_uri([])
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('state', qs.keys())
        self.assertEqual(state, qs['state'][0])
           
    # code_challenge
    def test_generate_url_code_challenge(self) -> None:
        code_challenge = "test_code_challenge"
        
        # need to workout how to mock a module when i get internet
        
        uri = self.api_security._get_auth_uri([])
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('code_challenge', qs.keys())
        self.assertEqual(code_challenge, qs['code_challenge'][0])
    
    # code_challenge_method
    def test_generate_url_code_challenge_method(self) -> None:
        code_challenge_method = "S256"
        
        uri = self.api_security._get_auth_uri([])
        qs = parse_qs(urlparse(uri).query)
        
        self.assertIn('code_challenge_method', qs.keys())
        self.assertEqual(code_challenge_method, qs['code_challenge_method'][0])
        
    ### _generate_state
    def test_generate_state(self) -> None:
        pass
    
    
class TestNotSureIfWeNeed(unittest.TestCase):    
    # other tests that might need implementing
    def test_login_starts_http_server_for_response(self) -> None:
        self.skipTest("Not Implemented")
        
    def test_login_checks_state_response(self) -> None:
        self.skipTest("Not Implemented")
        
    def test_login_opens_browser_with_correct_uri(self) -> None:
        self.skipTest("Not Implemented")
        
    def test_login_returns_token_with_claims(self) -> None:
        self.skipTest("Not Implemented")


if __name__ == '__main__':
    unittest.main()
