from flask import Flask, g, jsonify, request, send_file
import sqlite3

from queries import test_run_query, run_query

app = Flask(__name__)

DATABASE = '/opt/unstabletwin/database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    return '', 404


@app.route('/api')
def hello_api():
    return '', 404


@app.route('/api/login',  methods=['POST'])
def hello_login_get():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    d = run_query(db, username, password)
    # print(d)
    return jsonify(d)


@app.route('/info')
def hello_info():
    d = "The login API needs to be called with the username and password form fields fields.  " \
        "It has not been fully tested yet so may not be full developed and secure"
    return jsonify(d), 200, {'Build Number': '1.3.4-dev', 'Server Name': "Vincent"}


@app.route('/get_image')
def get_image():
    if request.args.get('name').lower() == 'vincent':
        filename = 'Twins-Danny-DeVito.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'julias':
        filename = 'Twins-Arnold-Schwarzenegger.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'mary_ann':
        filename = 'Twins-Bonnie-Bartlett.jpg'
        return send_file(filename, mimetype='image/gif')
    return '', 404

#@app.route('/test')
#def test_api():
#    db = get_db()
#    test_run_query(db)
#    return '', 404


if __name__ == '__main__':
    app.run(port=5001)
