from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {"id": "1", "task": "Task"},
    {"id": "2", "task": "Task2"},
    {"id": "3", "task": "Task3"},
]


@app.get("/")
def index():
    print(todos)
    return render_template("todo_list/todo_list.htm", todos=todos)


@app.post("/add")
def add_task():
    global todos
    print(request.form["new_task"])
    todos.append({"id": '4', "task": request.form["new_task"]})
    return redirect(url_for("index"))


@app.post("/delete")
def delete_task():
    global todos
    ids = request.form.getlist("task")
    print(ids)
    todos = list(filter(
        lambda item: True if not item["id"] in ids else False, todos))
    return redirect(url_for("index"))
