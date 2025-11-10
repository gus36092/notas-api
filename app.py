from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "vladi es el mas venenoso del mundo mundial for ever"})

if __name__ == "__main__":
    app.run(debug=True)
