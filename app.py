#!/usr/bin/env python3
from flask import Flask,render_template, request
from jinja2 import Template
import utils
app = Flask(__name__)

@app.route('/')
def template_test():
    return render_template('home.html')

@app.route('/search/',methods = ['POST', 'GET'])
def search():
     if request.method == 'GET' and bool(request.args):
        result = request.args["search"]
        result_render = utils.findUnicode(result)
        return render_template("result.html",len = len(result_render),result_render=result_render)
     else:
        return render_template('search.html')

@app.route('/list/')
def list_all():
    result_render = utils.getAllInformations()
    print(result_render)
    return render_template("list.html",len = len(result_render),tabs=result_render)
  
@app.route('/unicode/<codepoint>')
def matchsasa_uni(codepoint):
    print(codepoint)
    resultUniqueUni = utils.UniqueUni(codepoint)
    return render_template('simpleresult.html', name=resultUniqueUni['name'],number=resultUniqueUni['number'],cat=resultUniqueUni['cat'])