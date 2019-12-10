import unittest 
from ToDoApp import app
import requests, json

class test_toDoApp(unittest.TestCase):

    def setUp(self):
        app.config["MONGO_URI"] = "mongodb+srv://m220student:m220password@flask-wrhs8.mongodb.net/test?retryWrites=true&w=majority"
        self.client = app.test_client()       
    def test_get_task(self):
        result = self.client.get("http://127.0.0.1:5000//todo/api/v1.0/tasks")
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()