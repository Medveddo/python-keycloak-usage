<script>
  import { onMount } from "svelte";
  import Keycloak from "keycloak-js";

  let keycloakglobal = {}
  let userInfo = {}

  onMount(() => {
    let keycloak = new Keycloak({
      url: "http://localhost:8080",
      realm: "myrealm",
      clientId: "myclient",
    });

    keycloak
      .init({ onLoad: "login-required" })
      .then(function (authenticated) {
        console.info("User successfully authenticated");
        userInfo.name = keycloak.tokenParsed.name
        userInfo.tokenParsed = keycloak.tokenParsed
        userInfo.token = keycloak.token
        keycloakglobal = keycloak
      })
      .catch(function (e) {
        console.error(e);
      });
    console.log(keycloak);
  });
  function keycloakSignOut() {
    keycloakglobal.logout();
  }
  function getStatus() {
    console.log(keycloakglobal);
  }
</script>

<h3>User info</h3>
<p>
    Name: {userInfo.name}
    <br>
    <br>
    Token: {userInfo.token}
    <br>
    <br>
    tokenParsed: {JSON.stringify(userInfo.tokenParsed)}
    
</p>
<button on:click={keycloakSignOut}>Sign Out</button>
