import os
from lesson_3.widget import main

env_app = "TEST"

def set_env():
    if "APP_ENV" not in os.environ:
        os.environ["APP_ENV"] = env_app

if __name__ == "__main__":
    set_env()
    main()
