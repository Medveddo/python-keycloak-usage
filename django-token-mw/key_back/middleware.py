from typing import Any, Optional, Tuple
from django.http import HttpRequest, HttpResponse

from django.contrib.auth import login
from django.contrib.auth.models import User

from keycloak import KeycloakOpenID

class KeycloakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        auth_token, response = self._get_auth_token(request)
        if response:
            return response

        parsed_token, response = self._parse_token(auth_token)
        if response:
            return response

        user, created = User.objects.get_or_create(username=parsed_token['preferred_username'], first_name=parsed_token["given_name"], last_name=parsed_token["family_name"])
        
        print(user.first_name)
        print(user.last_name)
        print(user.username)

        login(request, user)

        response = self.get_response(request)


        # Code to be executed for each request/response after
        # the view is called.

        return response

    def _get_auth_token(self, request: HttpRequest) -> Tuple[str, Optional[HttpResponse]]:
        response = None
        auth_token = ""
        if "Authorization" not in request.headers:
            response = HttpResponse("401 Unauthorized", status=401)
            return auth_token, response
        
        print(request.headers["Authorization"])
        
        if "Bearer " not in request.headers["Authorization"]:
            response = HttpResponse("400 Bad Request - Bearer token required", status=400)
            return auth_token, response

        auth_token = request.headers["Authorization"].removeprefix("Bearer ")
        
        print(auth_token)

        return auth_token, response

    def _parse_token(self, auth_token) -> Tuple[dict, Optional[HttpResponse]]:
        response = None
        parsed_token = {}
        
        keycloak_open_id = KeycloakOpenID(
            server_url="http://localhost:8080",
            realm_name="myrealm",
            client_id="myclient",
            verify=False,  # TLS
        )
        keycloak_public_key = (
            "-----BEGIN PUBLIC KEY-----\n"
            + keycloak_open_id.public_key()
            + "\n-----END PUBLIC KEY-----"
        )

        options = {
            #     "verify_signature": False,  # jose.exceptions.ExpiredSignatureError: Signature has expired. - OK
            "verify_aud": False,  # jose.exceptions.JWTClaimsError: Invalid audience ???
            #     "verify_exp": False,
        }

        try:
            parsed_token = keycloak_open_id.decode_token(
                auth_token, keycloak_public_key, options=options
            )
        except Exception as e:
            print(e)
            response = HttpResponse(f"401 Unauthorized - {e}", status=401)
            return {}, response
        
        print(parsed_token)

        return parsed_token, response
