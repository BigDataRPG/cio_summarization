from flask import render_template, send_from_directory, request
from __init__ import *

import os

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        """
        SEARCH PROCESS
            searchKeyWordsByPeriod(): 
                return: json form
            response: chunk of result, size = 15 (check on searchKeyWordsByPeriod())
        """
        date_from, date_to, key_word = request.form['dateFrom'], request.form['dateTo'], request.form['keyWord']

    total_result = LongNews.query.count()
    left_result_query = LongNews.query.filter_by(flg_done=0)
    left_result_obj = left_result_query.all()

    """
        สำหรับไปแสดงผลที่หน้า VIEW
    """
    left_result_dct = {}
    for left_result_ in left_result_obj:
        left_result_dct[left_result_.luid] = left_result_.body.split("<EDU>")

    flg_model_dct = {}
    for left_result_ in left_result_obj:
        flg_model_dct[left_result_.luid] = str(left_result_.flg_model)

    flg_human_dct = {}
    for left_result_ in left_result_obj:
        flg_human_dct[left_result_.luid] = str(left_result_.flg_human)

    left_result = left_result_query.count()
    done_result = total_result - left_result

    return render_template('home.html', **locals(), zip=zip)


@app.route('/about')
def about():

    return render_template('about.html', **locals(), zip=zip)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico')
