# :warning: Important Information [NOT RECOMMENDED]
Although this application allows running without any webserver in front of gunicorn it is heavily recommended by almost 
everyone **not** to do this. It is hard to find exact explanations and appears not to be a security but only
a performance risk but that is just my personal interpretation.

**If you dont know what you are doing please choose the traefik-nginx config**

----

Please refer to the traefik documentation on how to setup a docker service in traefik. Since treafik can be a little
confusing at times, the following are examples of my traefik configuration.


You need to create a network called `traefik` using `docker network create traefik`.
## docker-compose.yml

```
version: "3.3"

services:

  traefik:
    image: "traefik:v2.1"
    container_name: "traefik"
    ports:
      - "443:443"
      - "80:80"
      - "8080:8080"
    volumes:
      - "./letsencrypt:/letsencrypt"
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./config:/etc/traefik/"


networks:
    default:
       external:
         name: traefik
```

## traefik.toml
Place this in a directory called `config` as this is mounted into the traefik container (see docer compose).
**Change the email address accordingly**.
```
[api]
  insecure=true

[providers.docker]
  endpoint = "unix:///var/run/docker.sock"
  exposedByDefault = false
  network = "traefik"

#[log]
#  level = "DEBUG"

[entryPoints]
  [entryPoints.web]
    address = ":80"

  [entryPoints.web_secure]
    address = ":443"

[certificatesResolvers.le_resolver.acme]

  email = "you_email@mail.com"
  storage = "/letsencrypt/acme.json"

  tlsChallenge=true
```