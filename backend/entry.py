from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class CalendarEvent(Resource):
    def get(self):
        resp = jsonify({'status-testing': 'ok'})
        return resp
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

api.add_resource(CalendarEvent, '/event')
if __name__ == '__main__':
    app.run()