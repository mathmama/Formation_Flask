from flask import Flask

app = Flask(__name__)

# Le décorateur route() dans Flask est utilisé pour lier l'URL à une fonction
@app.route('/')
def Hello_world():
	return '<h1>Hello world !!</h1>'
# on peut aussi utilise la fonction : add_url_rule :
#app.add_url_rule('/', 'hello', Hello_world)

#Il est possible de créer une URL de manière dynamique, en ajoutant des parties variables au paramètre de règle
@app.route('/hello/<username>')
def Hello_user(username):
	return '<h1> Hello %s !! </h1>' % username
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'






if __name__ == '__main__':
	app.run(debug=True)