from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
db = SQLAlchemy(app)

class Pile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marktext = db.Column(db.String(30), nullable=False)
    number = db.Column(db.Integer, nullable=False)

db.create_all()

# DB作成後の1度だけ必要な処理
marktexts = ['heart', 'club', 'dia', 'spade']
numbers = range(1, 14)
for marktext in marktexts:
    for number in numbers:
        new_card = Pile(marktext=marktext, number=number)
        db.session.add(new_card)
        db.session.commit()


# 実行
# python cards.py

# cards.dbの作成
# >>> python
# >>> from cards import db
# >>> db.create_all()
