from flask_sqlalchemy import SQLAlchemy
from flask.json import JSONEncoder

db = SQLAlchemy()


class TodoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Todo):
            return {
                'id': obj.id,
                'content': obj.content,
            }
        return super(TodoJSONEncoder, self).default(obj)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        show_len = 20
        return self.content if len(self.content) < show_len else f'{self.content}...'
