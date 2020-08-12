from flask import Flask , redirect, url_for, render_template

app =Flask(__name__) 

@app.route('/index/<int:score>')
def index(score):
	#return '<html><title>home page </title><body><h1>this is home page , you welcome </h1></body></html>'
	return render_template('index.html',marks = score)

if __name__ == '__main__':
	app.run(debug=True)