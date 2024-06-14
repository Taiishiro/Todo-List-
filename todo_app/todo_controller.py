from flask import Flask, render_template, request, redirect, url_for
from todo_model import Tache

app = Flask(__name__)

@app.route("/")
def index():
    tasks = Tache.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    description = request.form["description"]
    Tache.add_task(task, description)
    return redirect(url_for("index"))

@app.route("/remove/<int:task_id>")
def remove_task(task_id):
    Tache.remove_task(task_id)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    Tache.complete_task(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
