from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

tasks = {
    "To-Do": [],
    "In Progress": [],
    "Done": [],
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        action = request.form.get('action')
        from_list = request.form.get('from')
        to_list = request.form.get('to')

        if action == 'add':
            tasks['To-Do'].append(task)
        elif action == 'move' and task in tasks[from_list]:
            tasks[from_list].remove(task)
            tasks[to_list].append(task)
        elif action == 'delete' and task in tasks[from_list]:
            tasks[from_list].remove(task)
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
