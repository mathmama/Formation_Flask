from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/user/<username>')
def success(username):
	return '<h1> Welcome to home page %s </h>' % username

@app.route('/login',methods = ['POST','GET'])
def login():
	if request.method =='POST':
		name = request.form['name']
		pas = request.form['pass']

		if pas=='rachid':
			return redirect(url_for('success',username=name))
		else:
			return '<h1> access denied for %s ,check your username and password' % name

	else:
		name = request.args.get('name')
		pas = request.args.get('pass')
		if pas=='rachid':
			return redirect(url_for('success',username=name))
		else:
			return '<h1> access denied for %s ,check your username and password' % name





if __name__ == '__main__':
	app.run(debug=True)