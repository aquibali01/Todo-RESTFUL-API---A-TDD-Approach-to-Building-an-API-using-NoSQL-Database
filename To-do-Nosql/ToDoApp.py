# importing all the libraries

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo 

app = Flask(__name__)

#connecting to the mongodb atlas
app.config["MONGO_URI"] = "mongodb+srv://m220student:m220password@flask-wrhs8.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

# Adding the Task to the database

@app.route("/addTasks")
def addTasks():
    task = mongo.db.toDoApp
    task.insert(
        {"id" : 0,
        "title" : "Meeting with client",
        "description" : "The Meeting is with Mr. Ali @ 11 A.M",
        "done": False}
        )
    return "Task(s) Added"
    @app.route("/todo/api/v1.0/tasks")
    def get_all_tasks(self):
        return jsonify({"task" : data})        


if __name__ == "__main__":
    app.run(debug=True)