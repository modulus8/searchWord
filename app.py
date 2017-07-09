#-*- coding:itf-8 -*-

import os
from bottle import route, run

@route("/")
def hello():
	return "Hello"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
