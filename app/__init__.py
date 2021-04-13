from flask import Flask

app = Flask(__name__)

from app import routes  # here, to prevent circular imports // why not at the top

