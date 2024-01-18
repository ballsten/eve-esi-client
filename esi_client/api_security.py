from oauthlib.oauth2 import WebApplicationClient
from pkce import generate_pkce_pair
import webbrowser
from urllib.parse import urlparse, parse_qs
from urllib3 import PoolManager
from jwt import decode, PyJWKClient

from http.server import BaseHTTPRequestHandler, HTTPServer

# borrowed concepts (and code) from https://www.camiloterevinto.com/post/oauth-pkce-flow-from-python-desktop
class OAuthHttpServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        HTTPServer.__init__(self, *args, **kwargs)
        self.authorization_code = ""

class OAuthHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<script type=\"application/javascript\">window.close();</script>".encode("UTF-8"))
        
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        
        self.server.authorization_code = qs["code"][0]
    
    # don't log to console
    def log_message(self, *args):
        pass

class ApiSecurity:
    """TODO: Docstring
    """

    def __init__(
        self,
        client_id,
        callback_uri
    ):
        self.client_id = client_id
        self.callback_uri = callback_uri
        self.port = urlparse(callback_uri).port or 80
        
        self._http = None # loaded lazily
        self._signing_key = None # loaded lazily
        
    def _get_jwt_public_key(self):
        jwks_client = PyJWKClient('https://login.eveonline.com/oauth/jwks')
        self._signing_key = jwks_client.get_signing_key('JWT-Signature-Key')
     
     
    def _get_auth_uri(self, scopes: [str]) -> str:
        """
        generates the authentication uri
        """
        client = WebApplicationClient(self.client_id)
        code_verifier, code_challenge = generate_pkce_pair()
        return client.prepare_request_uri(
            "https://login.eveonline.com/v2/oauth/authorize",
            redirect_uri=self.callback_uri,
            scope=scopes,
            state=self._generate_state(),
            code_challenge=code_challenge,
            code_challenge_method="S256"
            )
        
    def _generate_state(self) -> str:
        """
        generate a random 8 character string
        """
        pass
       
    def login(self, scopes: [str] = []):
        with OAuthHttpServer(('', self.port), OAuthHttpHandler) as httpd:
            
            webbrowser.open(self._get_auth_uri(scopes), new=2)
            
            auth_code = httpd.authorization_code
            
            data = {
                "code": auth_code,
                "client_id": self.client_id,
                "grant_type": "authorization_code",
                "code_verifier": code_verifier
            }
            
            response = self.http.request_encode_body(
                'POST', 
                'https://login.eveonline.com/v2/oauth/token', 
                fields=data, 
                encode_multipart=False
            )
            
            token = response.json()
            
            claims = decode(
                token['access_token'], 
                self._signing_key.key, 
                algorithms=['RS256'],
                audience='EVE Online',
                issuer='https://login.eveonline.com',
                options= {
                    'verify_iat': False
                }
            )
            token['claims'] = claims
            
            return token
        
        
            
            
            
            
            
            
            