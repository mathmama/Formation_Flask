from flask import Flask ,render_template,request
app = Flask(__name__)

@app.route('/')
def sign_up():
	return render_template('sign_up.html')

@app.route('/profil',methods = ['POST', 'GET'])
def profil():
	if request.method == 'POST':
		profil = request.form 
		return render_template('profil.html',profil=profil)



if __name__ == '__main__':
	app.run(debug = True)