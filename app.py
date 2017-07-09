#-*- coding:utf-8 -*-

import os
from bottle import route, run, static_file, view, request
from oxford import *
from weblio import *

@route("/")
@view('index')
def index():
	word = request.query.word
	weblio = Weblio(word)
	oxford = Oxford(word)
	return dict(word=word,weblio=weblio, oxford=oxford)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#run(host="localhost", port=3000, debug=True, reloader=True)
