from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class CalendarEvent(Resource):
    # Fetch event
    def get(self):
        resp = jsonify({'status-testing': 'ok'})
        return resp
    
    # Add event
    def post(self):
        data = request.get_json()

    # Update event
    def put(self):
        data = request.get_json()

    # Delete event
    def delete(self):
        data = request.get_json()
        
api.add_resource(CalendarEvent, '/event')

if __name__ == '__main__':
    app.run()