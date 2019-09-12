from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_todo/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        show_len = 20
        return self.content if len(self.content) < show_len else f'{self.content}...'


@app.route('/')
def hello_world():
    return 'Hello, World!'