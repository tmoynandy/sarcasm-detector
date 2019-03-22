from flask import Flask 
from flask import jsonify
from flask import g


app = Flask(__name__)


def get_loaded_model():
    loaded_model = None
    def get_model():
        nonlocal loaded_model
        if loaded_model is None:
            model = 'MODEL'
            '''load model here'''
            
        return loaded_model
    return get_model
get_loaded_model = get_loaded_model()


@app.route('/')
def index():
    return 'Server running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
