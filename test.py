from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only


app = Flask(__name__)
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
        return f"LongNews('{self.luid}', '{self.body}', '{self.summary}', " \
            f"'{self.flg_model}', '{self.flg_human}', '{self.flg_done}', '{self.flg_fix}')"


PATH_OILLONG = "/Users/redthegx/project/cio_summarization/oil_long/01022019.txt"

def preprocessing_text(text_edu):

    text_edu = text_edu.replace("\n","")
    text_edu = text_edu.replace("|", "<EDU>")

    return text_edu

def pharse_data_to_json(news_edu, text_ls):

    num_text = len(text_ls)
    num_rand_ls = []
    for _ in range(num_text):
        num_rand_ = str(random.randint(0,1))
        num_rand_ls.append(num_rand_)

    num_rand_str = "".join(num_rand_ls)

    news_pharse = LongNews(body=news_edu,
                  summary="",
                  flg_model=num_rand_str,
                  flg_human="",
                  flg_done=1,
                  flg_fix=0
                  )

    return news_pharse, num_rand_str

def order_by_random():
    return LongNews.query.order_by(func.random()).first()

if __name__ == "__main__":
    # with open(PATH_OILLONG, mode="r", encoding="utf-8") as file:
    #     data_line = file.readlines()
    #     data_ls = [preprocessing_text(edu) for edu in data_line]
    #     data_str = "".join(data_ls)
    #     news_pharse, num_rand_str = pharse_data_to_json(data_str, data_ls)
    #     db.session.add(news_pharse)
    #     db.session.commit()
    #     print(num_rand_str)



    # db.session.delete(news_1)
    # db.session.commit()
    # db.session.add(news_1)
    # db.session.commit()
    # all_data = LongNews.query().all().first()
    # db.session.delete(all_data)
    # db.session.commit()
    # for data in all_data:
    #     db.session.delete(data)
    #     db.session.commit()
    # print(obj)
    # for i in obj:
    #     print(i.body)
    # print(LongNews.query.filter_by(flg_done=0).all())
    # LongNews.query.filter_by(luid=1).delete()
    # db.session.commit()
    print(type(order_by_random()))
    print(order_by_random().luid)
    print(order_by_random().luid)
    print(order_by_random().luid)
    # left_result_query = LongNews.query.filter_by(flg_done=0)
    # left_result_obj = left_result_query.all()
    # for left_result_ in left_result_obj:
    #     print(left_result_.luid)

    # left_result_ls = [left_result_.body.split("<EDU>") for left_result_ in left_result_obj]
    # print(left_result_obj[0].flg_model)
