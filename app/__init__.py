from flask import Flask

app = Flask(__name__)

todos = []

from app import routes
