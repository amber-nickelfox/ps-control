import sys
from flask import Flask, jsonify, render_template, session

SERVER_PORT = '8080'  # modify this to set server to run on a different port

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-powerpoint-game-is-strong'
app.debug = False


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/command/")
def command():
    keyboard_command = session['command']
    return_value = jsonify({'command': keyboard_command})
    return return_value


@app.route("/set-next/")
def set_next():
    keyboard_command = 'next'
    session['command'] = keyboard_command
    return jsonify({'command': keyboard_command})


@app.route("/set-back/")
def set_back():
    keyboard_command = 'back'
    session['command'] = keyboard_command
    print("User press back")
    return jsonify({'command': keyboard_command})


def main(argv):
    app.run(host='0.0.0.0', port=SERVER_PORT)


if __name__ == '__main__':
    main(sys.argv[1:])
