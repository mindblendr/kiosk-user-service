# USER SERVICE

This is user-service.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install from requirements.txt.

```bash
pip install -r requirements.txt
```

If there are changes in the dependencies, always update the requirements.txt

```bash
pip freeze > requirements.txt
```

## Starting The Service

Run the application using [uvicorn](https://www.uvicorn.org/)

```bash
python main.py
```

## Running local redis servers

In order to test locally, you need 2 redis servers. 1 for session caching, and another for the pubsub

```bash
docker run --name <REDIS_SERVER_NAME> -p <PUBLIC_PORT>:6379 -d redis
```