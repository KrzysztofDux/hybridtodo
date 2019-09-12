from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from .todo import Todo, TodoJSONEncoder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_todo/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json_encoder = TodoJSONEncoder

db = SQLAlchemy(app)


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        new_todo = create_todo(request.form['content'])
        return jsonify(new_todo)
    elif request.method == 'GET':
        return handle_get_todo(request)


def create_todo(content):
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return new_todo


def handle_get_todo(get_request):
    if "id" in get_request.args:
        return get_specific_todo(get_request.args.get("id"))
    else:
        return get_all_todos()


def get_specific_todo(todo_id):
    return jsonify(Todo.query.filter_by(id=todo_id).first())


def get_all_todos():
    return jsonify(Todo.query.all())
