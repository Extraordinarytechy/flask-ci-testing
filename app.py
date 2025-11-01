from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API Running Successfully"}), 200

@app.route('/add')
def add_numbers():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({"result": a + b}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
