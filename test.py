from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///summary.sqlite3"
SQLALCHEMY_DATABASE_URI = "sqlite:////Users/redthegx/project/cio_summarization/sqlite-tools-osx-x86-3290000/summary.db"

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
        return f"LongNews('{self.luid}', '{self.flg_done}', '{self.flg_fix}')"

# class ShortNews(db.Model):
#    lid = db.Column('long_id', db.Integer, primary_key=True, nullable=False)
#    body = db.Column(db.Text, nullable=False)
#    summary = db.Column(db.String, nullable=False)
#    flg_model = db.Column(db.Integer, nullable=False)
#    flg_human = db.Column(db.Integer, nullable=False)
#
#    def __init__(self, lid, body, summary):
#       self.lid = lid
#       self.body = body
#       self.summary = summary
#
#    def __repr__(self):
#       return f"ShortNews('{self.lid}', '{self.flg_model}', '{self.flg_human}')"

# db.create_all()
#
news_1 = LongNews(body="ความซ้ำซ้อน (ความซ้ำซ้อน; ในภาษาอังกฤษ",
                  summary="ความซ้ำซ้อน (ความซ้ำซ้อน; ในภาษาอังกฤษ",
                  flg_model="1,0,0",
                  flg_human="1,1,0",
                  flg_done=1,
                  flg_fix=0
                  )

# db.session.commit()


if __name__ == "__main__":
    # db.session.add(news_1)
    # db.session.commit()
    obj = LongNews.query.filter_by(flg_done=1).all()
    print(obj)
    # for i in obj:
    #     print(i.body)
    # print(LongNews.query.filter_by(flg_done=1).first())