from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
db = SQLAlchemy(app)
# db.create_all()

class Pile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marktext = db.Column(db.String(30), nullable=False)
    number = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    cards = Pile.query.all()
    # cards = Pile.query.order_by(Pile.due.desc())    # 降順
    return render_template('index.html', cards=cards, today=date.today())


if __name__ == "__main__":
    app.run(debug=True)


# 実行
# python cards.py

# cards.dbの作成
# >>> python
# >>> from cards import db
# >>> db.create_all()
