from typing import Dict

from fastapi import FastAPI, Request

from oidc_auth.auth import OpenIDConnect

# realm (e.g. Keycloak instance)
host = "http://localhost:8080"
realm = "myrealm"
client_id = "conf-client"
client_secret = "I4rSpkw7Dp7sHVgMWYzwboStV9DotTTp"
app_uri = "http://localhost:8000"

oidc = OpenIDConnect(host, realm, app_uri, client_id, client_secret)
app = FastAPI()

@app.get("/")
@oidc.require_login
async def very_secret(request: Request) -> Dict:
    return {"message": "success", "user_info": request.user_info}
