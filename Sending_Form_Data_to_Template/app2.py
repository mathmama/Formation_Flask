from flask import Flask ,render_template,request
app = Flask(__name__)

@app.route('/')
def sign_up():
	render_template('sign_up.html')



if __name__ == '__main__':
	app.run(debug = True)