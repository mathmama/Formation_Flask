from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filee():
	file = request.files['file']
	if request.method == 'POST':
	  filename = secure_filename(file.filename)
	  f = request.files['file']
	  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	  return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)