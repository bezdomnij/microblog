from flask import Flask
from config import Config  # adding config class / import from config module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  # import config from Config class
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models  # here, to prevent circular imports // why not at the top
