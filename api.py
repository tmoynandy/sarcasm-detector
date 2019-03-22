from flask import Flask 
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
