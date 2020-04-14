# python-flask-mongoengine-docker-starter

[![Language](https://img.shields.io/badge/language-python3-brightgreen)](https://www.python.org/)
[![License](https://img.shields.io/github/license/michaljach/python-flask-mongoengine-docker-starter)](https://opensource.org/licenses/MIT)
[![Repo size](https://img.shields.io/github/repo-size/michaljach/python-flask-mongoengine-docker-starter)](https://github.com/michaljach/python-flask-mongoengine-docker-starter)

This is a starter or boilerplate to create RESTful API with Python and MongoDB using Flask microframework. The project uses Docker (docker-compose) for easy to use, encapsulated and safe environment.

## Stack

- Python 3
- Flask
- Flask-RESTPlus
- Mongoengine
- Unittest
- Docker
- Swagger

## Usage

[Install Docker](https://www.docker.com/products/docker-desktop) if you don't have it yet and run the container:

```sh
$ docker-compose up
```

It will run both Web and Mongodb containers in Development environment on `localhost:5100`.
For other environments change ENV in `docker-compose.yml`:

```sh
web:
   ...
    environment:
      - ENV=Testing
```

You can use Development, Production or Testing or add your own environment in `api/config.py`.

## Structure

Here is a folder and file structure with explanation.

```
├── Dockerfile
├── LICENSE
├── README.md
├── api
│   ├── app.py - Entry point of application
│   ├── config.py - Configuration with environments
│   └── v1 - API version 1
│       ├── database
│       │   └── models.py - All data models app uses
│       └── resources
│           ├── routes.py - List of namespaces for routing
│           └── todos.py - Example Todo resource
├── docker-compose.yml
├── requirements.txt - Dependencies
└── tests
    └── text_base.py - Example test file
```

## Documentation

Thanks to handy decorators this boilerplate will generate Swagger with documentation on the fly.
By default Swagger runs on `/` so you should see it on `http://localhost:5100`. Read more [here](https://flask-restplus.readthedocs.io/en/stable/swagger.html).

![Swagger](https://i.imgur.com/G7EbHK4.png)

## Testing

You can run tests easily within Docker container:

```
docker-compose run web python tests/test_base.py
```

## License

See LICENSE file.
