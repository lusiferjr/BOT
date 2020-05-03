import flask
from flask import request, jsonify, request
import mysql.connector
# from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# database connection

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'test'

# mysql = MySQL(app)

# if request.method == "POST":
#     details = request.form
#     firstName = details['fname']
#     lastName = details['lname']
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
#     mysql.connection.commit()
#     cur.close()
#     return 'success'
# return render_template('index.html')
# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'}
]


@app.route('/', methods=['GET'])
def home()
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/data', methods=['GET'])
def databaseconnect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="test"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM hello")
    temp = []
    for x in mycursor:
        temp.append(x)
    return jsonify(temp)


app.run(host='0.0.0.0', port='5002')
