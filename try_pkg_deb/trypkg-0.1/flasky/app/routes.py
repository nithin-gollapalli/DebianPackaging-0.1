from app import app

@app.route('/')
@app.route('/index')
def index():
	return '<h2>Hello World!</h2>'
