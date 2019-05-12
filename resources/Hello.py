from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {'message': 'Hello, World! (GET)'}

    def post(self):
        return {'message': 'Hello, World! (POST)'}
        