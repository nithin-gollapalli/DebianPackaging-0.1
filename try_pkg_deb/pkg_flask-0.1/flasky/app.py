from flasky import my_app

@my_app.route('/')
@my_app.route('/index')
def index():
	return '<h1>Welcome One and All<h1>'

@my_app.route('/route')
def route():
	import os
	return '<h3>%s</h3>'%(os.getcwd())
