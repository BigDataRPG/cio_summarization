from flask import render_template, send_from_directory, request
from __init__ import *
import os

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        """
        GET AND POST PROCESS
            
        """
        date_from, date_to, key_word = request.form['dateFrom'], request.form['dateTo'], request.form['keyWord']

    """
        สำหรับไปแสดงผลที่หน้า VIEW
    """
    result_left = query_order_by_random()
    result_left_edu_ls = result_left.body.split("<EDU>")
    result_left_flg_model_ls = str(result_left.flg_model)
    result_left_flg_humna_ls = str(result_left.flg_human)

    """
        PATH ของการคำนวณ จำนวนที่เหลือจากการ Track
    """
    result_total = LongNews.query.count()
    result_total_left = LongNews.query.filter_by(flg_done=0).count()
    result_total_done = result_total - result_total_left


    # flg_model_dct = {}
    # for left_result_ in left_result_obj:
    #     flg_model_dct[left_result_.luid] = str(left_result_.flg_model)
    #
    # flg_human_dct = {}
    # for left_result_ in left_result_obj:
    #     flg_human_dct[left_result_.luid] = str(left_result_.flg_human)


    return render_template('home.html', **locals(), zip=zip)


@app.route('/about')
def about():

    return render_template('about.html', **locals(), zip=zip)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico')
