import sys
from flask import Flask, jsonify, render_template, session

SERVER_PORT = '8080'  # modify this to set server to run on a different port

COMMAND = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-powerpoint-game-is-strong'
app.debug = False


@app.route("/", methods=['GET'])
def index():
    global COMMAND
    return render_template('index.html')


@app.route("/command/")
def command():
    global COMMAND
    value = jsonify({'command': COMMAND})
    COMMAND = None
    return value


@app.route("/set-next/")
def set_next():
    global COMMAND
    COMMAND = 'next'
    return jsonify({'command': COMMAND})


@app.route("/set-back/")
def set_back():
    global COMMAND
    COMMAND = 'back'
    return jsonify({'command': COMMAND})


def main(argv):
    app.run(host='0.0.0.0', port=SERVER_PORT)


if __name__ == '__main__':
    main(sys.argv[1:])
