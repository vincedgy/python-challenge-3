# API HOUR !

A simple REST API using SQLite and FastAPI.


# Requirements

Python 3.9+


# Install


## Activate virtual env for python3

```sh
python3 -m venv .venv && source .venv/bin/activate
```

## Install dependencies

```sh
pip install -r requirements.txt
```

## Run

```sh
python src/main.py
2021-06-16 23:18:50.471 | INFO     | __main__:run_api:9 - Démarrage de l'API REST pour API HOUR !
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [45869] using statreload
INFO:     Started server process [45871]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Swagger auto doc

The doc is auto generated !

- Using Swagger : [http://localhost:8080/docs](http://localhost:8080/docs)
- Using Redoc : [http://localhost:8080/redoc](http://localhost:8080/redoc)

You can also test with Swagger Editor
[https://editor.swagger.io/](https://editor.swagger.io/)

## Use postman

1. Install [postman](https://www.postman.com/downloads/)
2. Import Collection : `API HOUR Collection.postman_collection.json`
3. Import Postman environment : `API HOUR.postman_environment.json`

Enjoy !

## Using Tunnel for distance testing

Install [ngrok](https://ngrok.com/download)

```sh
$ ngrok http 8080

ngrok by @inconshreveable                                                                                                    (Ctrl+C to quit)
                                                                                                                                             
Session Status                online                                                                                                         
Session Expires               1 hour, 59 minutes                                                                                             
Version                       2.3.40                                                                                                         
Region                        United States (us)                                                                                             
Web Interface                 http://127.0.0.1:4040                                                                                          
Forwarding                    http://8953f315d2d0.ngrok.io -> http://localhost:8080                                                          
Forwarding                    https://8953f315d2d0.ngrok.io -> http://localhost:8080                                                         
                                                                                                                                             
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                    
                              0       0       0.00    0.00    0.00    0.00  
```