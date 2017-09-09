#-*- coding:utf-8 -*-

import os
from bottle import route, run, static_file, view, request, response
from oxford import *
from weblio import *

class Foo:pass

@route("/")
@view('index')
def index():
	# response.set_header('Cache-Control: private', 'max-age=86400')
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

@route("/add_example")
def add_example():
	word = request.query.word
	if word == "":
		add_list = ""
	else:
		example = get_example(word)
		add_list = "<ul>"
		for sentence in example:
			add_list += '<li class="example_list">' + sentence + '</li>'
		add_list += "	</ul>"
	return add_list

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
	print(response)
	print(str(dicti))
	return str(dicti)

#静的ファイルのルーティング
@route("/file/<filename:path>")
def static(filename):
	return static_file(filename, root="./static")


if __name__ == "__main__":
	if os.getenv("HEROKU")==None:
		run(host="192.168.1.6", port=3000, debug=True, reloader=True)
	else:
		run(host="0.0.0.0", port=(os.environ.get("PORT",5200)))
