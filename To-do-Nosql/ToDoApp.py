# importing all the libraries

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo 

app = Flask(__name__)

#connecting to the mongodb atlas
app.config["MONGO_URI"] = "mongodb+srv://m220student:m220password@flask-wrhs8.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

# Adding the Task to the database

@app.route("/todo/api/v1.0/addtasks")
def addTasks():
    task = mongo.db.toDoApp
    task.insert(
        {"id" : 0,
        "title" : "Meeting with client",
        "description" : "The Meeting is with Mr. Ali @ 11 A.M",
        "done": False}
        )
    task.insert(
        {"id" : 1,
        "title" : "Brother's Birthday",
        "description" : "Have to wish Haris a birthday",
        "done": False}
        )
    
    return "Task(s) Added"

# Retrieving lists of tasks from the database

@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def get_all_tasks():
    data = mongo.db.toDoApp
    tasks = data.find({}, {"_id": 0})
    task_list = []
    for task in tasks:
        task_list.append(task)
    return jsonify({"task" : task_list})   

# Retrieving a task from the database
@app.route("/todo/api/v1.0/tasks/<int:id>", methods=["GET"])
def get_a_task(id):
    data = mongo.db.toDoApp
    task = data.find_one({"id": id},{"_id": 0})
    return jsonify({"task" : task})
    


if __name__ == "__main__":
    app.run(debug=True)