import unittest
import json
from app import app

class TodoListApiTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_tasks(self):
        response = self.app.get('/api/tasks')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_get_task_by_id(self):
        task_id = 1
        response = self.app.get(f'/api/tasks/{task_id}')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], task_id)

    def test_get_task_by_invalid_id(self):
        invalid_id = 1000
        response = self.app.get(f'/api/tasks/{invalid_id}')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Task not found', data['message'])

if __name__ == '__main__':
    unittest.main()