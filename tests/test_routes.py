import unittest
from app import app, todos


class ToDoTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        todos.clear()  # Clear todos list before each test

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ToDo List', response.data)

    def test_add_todo(self):
        response = self.app.post('/add', data=dict(todo='Test ToDo'))
        self.assertEqual(response.status_code, 302)  # Redirection after adding
        response = self.app.get('/')
        self.assertIn(b'Test ToDo', response.data)

    def test_delete_todo(self):
        # Add a ToDo first
        self.app.post('/add', data=dict(todo='Test ToDo'))
        response = self.app.post('/delete/0')
        self.assertEqual(response.status_code, 302)  # Redirection after deleting
        response = self.app.get('/')
        self.assertNotIn(b'Test ToDo', response.data)


if __name__ == '__main__':
    unittest.main()
