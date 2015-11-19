##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

from flask import Flask, request
from werkzeug import secure_filename
from process import Processer
import os
processer = Processer()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def status():
	return "true"

@app.route("/process", methods=["POST"])
def process():
	print request
	file = request.files['file']
	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		match = processer.compare(os.path.join("./uploads/", filename))
		return match
	return ""

app.config['UPLOAD_FOLDER'] = "./uploads/"

if __name__ == "__main__":	
	print processer.compare("./tests/a.png")
	app.run(host="0.0.0.0",debug=True)
