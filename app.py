from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
	return '<h1>Welcome to home page'

if __name__ == '__main__':
	app.run()