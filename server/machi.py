import fuckcsv
import flask
from flask import request, jsonify, request

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
        obj.plot(graphType,col1,col2)

@app.route('/csv/plotGraph/single',methods=['Post'])
def csv_plotsingle():
    obj=fuckcsv.Csv("train.csv")
    if request.method == "POST":
        details = request.form
        graphType = details['graphType']
        col1 = details['col1']
        col2 = details['col2']
        obj.plot(graphType,col1,col2)
def
app.run(host='0.0.0.0', port='5000')
