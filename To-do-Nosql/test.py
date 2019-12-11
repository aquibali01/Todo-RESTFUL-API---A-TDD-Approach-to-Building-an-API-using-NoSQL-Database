import unittest 
from ToDoApp import app
import requests, json

class test_toDoApp(unittest.TestCase):

    def setUp(self):
        app.config["MONGO_URI"] = "mongodb+srv://m220student:m220password@flask-wrhs8.mongodb.net/test?retryWrites=true&w=majority"
        self.client = app.test_client()   

    # testing adding tasks functionality
    def test_post_task(self):
        result = self.client.post("http://127.0.0.1:5000//todo/api/v1.0/tasks",
                                data = json.dumps({
                                                "id" : 3,
                                                "title" : "Dinner outside",
                                                "description" : "have a dinner with family",
                                                "done": True}),
                                                content_type="application/json")
        self.assertEqual(result.status_code, 200)

    # testing retrieving all task functionality
    def test_get_tasks(self):
        result = self.client.get("http://127.0.0.1:5000//todo/api/v1.0/tasks")
        self.assertEqual(result.status_code, 200)

    # testing retrieving a task functionality
    def test_get_a_task(self):
        result = self.client.get("http://127.0.0.1:5000//todo/api/v1.0/tasks/1")
        self.assertEqual(result.status_code, 200)

        data = json.loads(result.data)
        self.assertEqual(data["task"]["title"], "Brother's Birthday")
        self.assertEqual(data["task"]["description"], "Have to wish Haris a birthday")

    # tesing a delete task functionality
    def test_delete_a_task(self):
        result = self.client.delete("http://127.0.0.1:5000//todo/api/v1.0/tasks/2")
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()