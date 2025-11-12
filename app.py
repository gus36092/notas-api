from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "Vlady-dev25 es el antidotoy Gustavo el mas poison del  mundo mundial for ever y cryador "})

if __name__ == "__main__":
    app.run(debug=True)
    