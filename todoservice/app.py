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
        todo_content = request.form['content']
        new_todo = Todo(content=todo_content)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo)
    elif request.method == 'GET':
        if "id" in request.args:
            return jsonify(Todo.query.filter_by(id=request.args.get("id")).first())
        else:
            return jsonify(Todo.query.all())
