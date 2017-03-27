from flask import Flask, request, render_template, url_for

@sb_web.route('/', methods=['get'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@sb_web.route('/about', methods=['get'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
