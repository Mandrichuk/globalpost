from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def main():
  data = {"members": ["John", "Paul", "Ringo", "George", "Mick", "Keith"]} 
  return jsonify(data)


if __name__ == "__main__":
  app.run(debug=True)