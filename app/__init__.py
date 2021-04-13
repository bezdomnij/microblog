from flask import Flask
from config import Config  # adding config class / import from config module

app = Flask(__name__)
app.config.from_object(Config)  # import config from Config class

from app import routes  # here, to prevent circular imports // why not at the top
