from flask import Flask, render_template,request,make_response
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/setcookie' , methods = ['POST' , 'GET'])
def setcookie():
	if request.method == 'POST' :
		user = request.form['Name']
		email = request.form['Email']
		resp = make_response(render_template('readcookie.html')) # pour obtenir un objet de réponse
		resp.set_cookie('userID',user) # pour stocker un cookie dans l'objet de réponse
		resp.set_cookie('Email',email)
		return resp

@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userID')
	email = request.cookies.get('Email')
	return '<h>Welcome '+name+'</h1> your email is %s' % email


if __name__ == '__main__':
	app.run(debug=True) 