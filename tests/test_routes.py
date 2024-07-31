# import os
import json
import unittest
from unittest.mock import patch, mock_open
from app import app
# from app.routes import save_todos, load_todos


class ToDoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.routes.open', new_callable=mock_open, read_data='[]')
    @patch('app.routes.os.path.exists', return_value=True)
    def test_add_todo(self, mock_exists, open_mock):
        with patch('app.routes.todos', []):
            response = self.app.post('/add', data=dict(todo='Test ToDo'))
            written_data = open_mock().write.mock_calls
            written_data_str = ''.join([call.args[0] for call in written_data])
            # print(f"Written data in test_add_todo: {written_data_str}")
            self.assertIn('Test ToDo', json.loads(written_data_str))

    @patch('app.routes.save_todos')
    @patch('app.routes.load_todos', return_value=["Test ToDo"])
    def test_delete_todo(self, mock_load, mock_save):
        with patch('app.routes.todos', ["Test ToDo"]):
            response = self.app.post('/delete/0')
            mock_save.assert_called()
            written_data = mock_save.call_args[0][0]
            # print(f"Written data in test_delete_todo: {written_data}")
            self.assertNotIn('Test ToDo', written_data)


if __name__ == '__main__':
    unittest.main()
