from flask import Flask, request, jsonify
import configparser
# Read config file
config = configparser.ConfigParser()
config.read('config.ini')
# Set global variables
GOOGLE_CREDENTIALS_KEY = config['API Keys']['google_credentials_key']
app = Flask(__name__)
# Debug mode ON!
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def hello_world():
    word = request.args.get('butt')
    return GOOGLE_CREDENTIALS_KEY


if __name__ == '__main__':
    app.run(host='0.0.0.0')
