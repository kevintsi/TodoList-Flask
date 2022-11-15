from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {"id": "1", "task": "Task"},
    {"id": "2", "task": "Task2"},
    {"id": "3", "task": "Task3"},
]


@app.get("/")
def index():

    return render_template("todo_list/todo_list.htm", todos=todos)


@app.post("/add")
def add_task():
    print(request.form["task"])
    todos.append({"id": 4, "task": request.form["task"]})
    return redirect(url_for("index"))


@app.delete("/delete")
def delete_task():
    pass
