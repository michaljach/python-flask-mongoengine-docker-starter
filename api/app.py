import json
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields
from mongoengine import Document, connect, StringField

app = Flask(__name__)
app.debug = True
connect('test', host='mongodb', port=27017)


api = Api(app)

ns = api.namespace('v1', description='TODO operations')


class Todo(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)


@ns.route('/todos')
class HelloWorld(Resource):
    def get(self):
        try:
            return json.loads(Todo.objects.all().to_json()), 200
        except:
            print("ec")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
