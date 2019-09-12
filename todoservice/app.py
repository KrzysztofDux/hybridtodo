from flask import Flask, request
from flask.json import jsonify, JSONEncoder
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_todo/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


class TodoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Todo):
            return {
                'id': obj.id,
                'content': obj.content,
            }
        return super(TodoJSONEncoder, self).default(obj)


app.json_encoder = TodoJSONEncoder


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        show_len = 20
        return self.content if len(self.content) < show_len else f'{self.content}...'
