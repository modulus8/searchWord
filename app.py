#-*- coding:utf-8 -*-

import os
from bottle import route, run, static_file, view, request, response
from oxford import *
from weblio import *

class Foo:pass

@route("/")
@view('index')
def index():
	response.set_header('Cache-Control: private', 'max-age=86400')
	print(response)
	word = request.query.word
	if word == "":
		weblio = Foo()
		oxford = Foo()
		weblio.title, weblio.translation, weblio.others, weblio.prediction_all = "None", "None", "None", {}
		oxford.title, oxford.pronounce, oxford.mp3 = "None", "None", "javascript:void(0)"
	else:
		weblio = Weblio(word)
		oxford = Oxford(word)
	return dict(word=word,weblio=weblio, oxford=oxford)

@route("/echo")
def echo():
	dicti = {
		"userAgent": request.get_header('User-Agent'),
		"requestMethod": request.method,
		"reqyestBody": request.body,
		"requestUrl": request.url,
		"requestUrlparts": request.urlparts,
		"requestRemoteAddr": request.remote_addr,
		"requestParams": request.params,
	}
	return str(dicti)

if __name__ == "__main__":
	if os.getenv("HEROKU")==None:
		run(host="192.168.1.6", port=3000, debug=True, reloader=True)
	else:
		run(host="0.0.0.0", port=(os.environ.get("PORT",5200)))

