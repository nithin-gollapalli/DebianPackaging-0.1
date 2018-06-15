from flasky import my_app

def run_server():
	my_app.debug = True
	return my_app

def dev_server():
	app = run_server()
	app.run()

if __name__ == '__main__':
	dev_server()
