from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class HelloPerson(Resource):
	def get(self):
		return jsonify([
			{'firstName': 'Max', 'lastName': 'Mustermann'},
			{'firstName': 'Kurt', 'lastName': 'Schnabel'}
		])

class HelloData(Resource):
	def get(self):
		return jsonify([
			{'fieldFirst': 1, 'fieldSecond': 2},
			{'fieldFirst': 3, 'fieldSecond': 4}
		])

api.add_resource(HelloWorld, '/')
api.add_resource(HelloPerson, '/persons')
api.add_resource(HelloData, '/data')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
