from v1.resources.todos import todos


def initialize_routes(api):
    api.add_namespace(todos)
