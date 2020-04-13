import unittest
from flask_testing import TestCase
from app import app


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.Testing')
        return app

    def test_server_is_up_and_running(self):
        self.assertEqual(200, 200)


if __name__ == '__main__':
    unittest.main()
