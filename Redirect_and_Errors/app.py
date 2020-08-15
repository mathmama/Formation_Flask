from flask import Flask , redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
	#print(request.method)
	if request.method == 'POST':
		if request.form['password'] == 'rachid' :
			return redirect(url_for('success'))
		else:
			abort(401)
	else:
		return redirect(url_for('index'))
@app.route('/success')
def success():
	return '<h1> Logged in successfully</h1>'

if __name__ == '__main__':
	app.run(debug=True)