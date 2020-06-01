# import fuckcsv
import flask
from flask import request, jsonify, request
import os
from werkzeug.utils import secure_filename
app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route('/csv/description', methods=['GET'])
def csv_description():
    obj = fuckcsv.Csv("train.csv")
    a = obj.describe()
    b = (
        {"error": "true"},
        {"message": "found"},
        {"info": a}
    )
    return jsonify(b)


@app.route('/csv/plotGraph/double', methods=['POST'])
def csv_plotdouble():
    obj = fuckcsv.Csv("train.csv")
    if request.method == "POST":
        details = request.form
        graphType = details['graphType']
        col1 = details['col1']
        col2 = details['col2']
        obj.plot(graphType, col1, col2)


@app.route('/csv/plotGraph/single', methods=['Post'])
def csv_plotsingle():
    obj = fuckcsv.Csv("train.csv")
    if request.method == "POST":
        details = request.form
        graphType = details['graphType']
        col1 = details['col1']
        col2 = details['col2']
        obj.plot(graphType, col1, col2)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['post'])
def upload_file():
    response = {"error": "true",
                "message": "message",
                "info": "info"
                }
    UPLOAD_FOLDER = r'X:\BOT\server\uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if 'file' not in request.files:
        response["error"] = "true"
        response["message"] = "file is missing"
        response["info"] = "no file found"
        return jsonify(response)
    file = request.files['file']
    if file.filename == '':
        response["error"] = "true"
        response["message"] = "file is missing"
        response["info"] = "no file found"
        return jsonify(response)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        response["error"] = "false"
        response["message"] = "file is recived"
        response["info"] = UPLOAD_FOLDER+"\\filename"
        return jsonify(response)



app.run(host='0.0.0.0', port='5000')
