from flask import Flask
from flask import send_file
import random

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(1, 22)
    return send_file(f"images/alberto_{number}.jpg", mimetype='image/gif')