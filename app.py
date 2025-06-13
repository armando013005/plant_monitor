from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
latest = {}

@app.route('/sensor', methods=['POST'])
def post_sensor():
    global latest
    latest = request.get_json()
    return '', 200

@app.route('/sensor/latest', methods=['GET'])
def get_sensor():
    return jsonify(latest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
