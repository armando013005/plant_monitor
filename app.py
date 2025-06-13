from flask import Flask, request, jsonify,render_template, json
from flask_cors import CORS

app = Flask(__name__)
app.config['TESTING'] = True 

CORS(app)
latest = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add_plant_info():
    plant = request.form.get()
    

@app.route('/sensor', methods=['POST'])
def post_sensor():
    global latest
    latest = request.get_json()
    return '', 200

@app.route('/sensor/latest', methods=['GET'])
def get_sensor():
    return jsonify(latest)

#TEST
@app.route("/")
def hello_world():
    return "<p>Hello, !</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
