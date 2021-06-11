from flask import Flask
from flask import send_file
import random
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        number = random.randint(1, 5)
        return send_file(f"images/alberto_{number}.jpg", mimetype='image/gif')

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)