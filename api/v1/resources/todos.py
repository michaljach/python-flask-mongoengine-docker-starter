import json
from flask import abort
from flask_restplus import Namespace, Resource
from v1.database.models import Todo
from mongoengine import DoesNotExist

todos = Namespace('v1/todos', description='Todos namespace')


@todos.route('/')
class TodosApi(Resource):
    def get(self):
        '''List all Todos'''
        todos = Todo.objects.all()
        return json.loads(todos.to_json()), 200


@todos.route('/<id>')
@todos.response(404, 'Todo not found')
@todos.param('id', 'The task identifier')
class TodoApi(Resource):
    def get(self, id):
        '''Fetch a given Todo'''
        try:
            todo = Todo.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)
