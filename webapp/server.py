import os
import json
from parser import parser
from bottle import route, template, redirect, run, error, request, response, static_file

@route('/')
def get_index():
    return template('index')

@route('/static/dist/<filename>')
def dist(filename):
    return static_file(filename, root='static/dist')

@route('/static/css/<filename>')
def css(filename):
    return static_file(filename, root='static/css')

@route('/static/image/<filename>')
def image(filename):
    return static_file(filename, root='static/image')

@route('/static/js/<filename>')
def js(filename):
    return static_file(filename, root='static/js')

@route('/static/json/<filename>')
def staticjson(filename):
    return static_file(filename, root='static/json')

@route('/getJSON', method="GET")
def getJSON():
    file_name = request.query["filename"]
    with open(f'database/{file_name}', 'r') as f:
        graph = json.load(f)
    res =  parser(graph['nodes'])
    print(res)
    return res

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
