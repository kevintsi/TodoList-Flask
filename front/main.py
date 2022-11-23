from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)

conn = mariadb.connect(
    host="localhost",
    database="todo_list",
    user="mariadb",
    password="password"
)


@app.get("/")
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM task")
    todos = cur.fetchall()
    print(todos)
    return render_template("todo_list/todo_list.htm", todos=todos)


@app.post("/add")
def add_task():
    if request.form["new_task"] == "":
        return redirect(url_for("index"))

    print(request.form["new_task"])
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO task (name) VALUES (?)",
                    (request.form["new_task"],))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error: {e}")

    return redirect(url_for("index"))


# @app.post("/delete")
# def delete_task():
#     ids = request.form.getlist("task")
#     print(ids)
#     cur = conn.cursor()
#     for id in ids:
#         try:
#             cur.execute("DELETE FROM task WHERE id = ?",
#                         (id,))
#             conn.commit()
#         except mariadb.Error as e:
#             print(f"Error: {e}")

#     return redirect(url_for("index"))
