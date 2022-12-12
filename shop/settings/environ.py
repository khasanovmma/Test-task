import os, environ

root = environ.Path(__file__) - 3
env = environ.Env()

ENV_FILE = os.getenv("WBNEWS_ENV", ".env.local")
environ.Env.read_env(ENV_FILE)
