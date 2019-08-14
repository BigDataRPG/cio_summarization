from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "sqlite:////Users/redthegx/project/cio_summarization/sqlite-tools-osx-x86-3290000/summary.db"
app.jinja_env.filters['zip'] = zip
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class LongNews(db.Model):

    __tablename__ = 'long_news'
    # lid = db.Column('long_id', db.Integer, primary_key=True, nullable=False)
    luid = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    flg_model = db.Column(db.Text, nullable=False)
    flg_human = db.Column(db.Text, nullable=False)
    flg_done = db.Column(db.Integer)
    flg_fix = db.Column(db.Integer)

    def __init__(self, body, summary, flg_model, flg_human, flg_done, flg_fix):
        self.body = body
        self.summary = summary
        self.flg_model = flg_model
        self.flg_human = flg_human
        self.flg_done = flg_done
        self.flg_fix = flg_fix

    def __repr__(self):
        return f"LongNews('{self.luid}', '{self.body}', '{self.summary}', " \
            f"'{self.flg_model}', '{self.flg_human}', '{self.flg_done}', '{self.flg_fix}')"

"""
DELETE ALL DATA IN SELECTED TABLE
    >> all_data = LongNews.query.all()
    >> for data in all_data:
        db.session.delete(data)
        print(data)
        db.session.commit()
"""
def order_by_random():
    return LongNews.query.order_by(func.random()).first()

if __name__ == "__main__":
    print(order_by_random)