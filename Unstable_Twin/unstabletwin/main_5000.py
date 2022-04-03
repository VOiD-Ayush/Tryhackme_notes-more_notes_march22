from flask import Flask, jsonify, request, send_file


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '', 404


@app.route('/api')
def hello_api():
    return '', 404


@app.route('/api/login',  methods=['POST'])
def hello_login():
    d = "The username or password passed are not correct."
    return jsonify(d)


@app.route('/info')
def hello_info():
    d = "The login API needs to be called with the username and password fields.  It has not been fully tested yet " \
        "so may not be full developed and secure"
    return jsonify(d), 200, {'Build Number': '1.3.6-final', 'Server Name': "Julias"}


@app.route('/get_image')
def get_image():
    if request.args.get('name').lower() == 'marnie':
        filename = 'Twins-Kelly-Preston.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'linda':
        filename = 'Twins-Chloe-Webb.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'mary_ann':
        filename = 'Twins-Bonnie-Bartlett.jpg'
        return send_file(filename, mimetype='image/gif')
    return '', 404


if __name__ == '__main__':
    app.run(port=5000)
