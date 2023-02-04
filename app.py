import json
from flask import jsonify, request
from sqlsessionapi import SQLSessionAPI
from task_list import TaskList
from task import Task
from _base import db, app

# INITIALISE DATABASE
api = SQLSessionAPI(db, app)
# back_log_task_list = TaskList(stage="Back Log")
# completed_task_list = TaskList(stage="Completed")
# api.write_value(back_log_task_list)
# api.write_value(completed_task_list)
# print(api.read_all_values(TaskList))

@app.route("/task", methods=["GET", "POST", "DELETE"])
def create_task():
    if request.method == "POST":
        task_data = json.loads(request.data.decode())
        task = Task(
            description=task_data["description"],
            title=task_data["title"],
            deadline=task_data["deadline"],
            SOP=task_data["SOP"],
            task_list_id=1
        )
        print(task)
        api.write_value(task)

    elif request.method == "DELETE":
        task_data = json.loads(request.data.decode())
        api.delete_value(Task, title=task_data["title"])
    else:
        return jsonify(list(filter(lambda task: task["task_list_id"] == 1,
                                   [task.public_attributes for task in api.read_all_values(Task)]
                                   )))

    print(api.read_all_values(Task))

    return {"res": "okay"}


@app.route("/task/complete", methods=["POST", "GET", "DELETE"])
def complete_task():
    if request.method == "POST":
        task_data = json.loads(request.data.decode())
        api.delete_value(Task, title=task_data["title"])
        task = Task(
            description=task_data["description"],
            title=task_data["title"],
            deadline=task_data["deadline"],
            SOP=task_data["SOP"],
            task_list_id=2
        )
        
        api.write_value(task)
        print(api.read_all_values(Task))
    elif request.method == "GET":
        return jsonify(list(filter(lambda task: task["task_list_id"] == 2,
                                   [task.public_attributes for task in api.read_all_values(Task)]
                                   )))

    elif request.method == "DELETE":
        for completed_task in api.read_all_values(Task):
            if completed_task.task_list_id == 2:
                api.delete_value(Task, title=completed_task.public_attributes["title"])
    else:
        pass

    print(api.read_all_values(Task))

    return {"res": "okay"}


if __name__ == "__main__":
    app.run(debug=True)
