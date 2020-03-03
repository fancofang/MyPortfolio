from Portfolio import app
from flask import render_template


@app.route('/')
@app.route('/intro')
def index():
    return render_template('index.html')


@app.route('/content')
def content():
    return render_template('main.html')


# @app.route('/content')
# def content():
#     return render_template('index111.html')