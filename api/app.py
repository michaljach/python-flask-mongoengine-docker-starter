import os
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.debug = True
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongodb/test'
}

db = MongoEngine(app)


class Todo(db.Document):
    title = db.StringField(max_length=60)
    content = db.StringField()


@app.route("/")
def index():
    Todo.objects().delete()  # Removes
    Todo(title="Simple todo A", content="12345678910").save()  # Insert
    Todo(title="Simple todo B", content="12345678910").save()  # Insert
    Todo.objects(title__contains="B").update(
        set__content="Hello world")  # Update
    todos = Todo.objects.all()
    return jsonify(todos), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
