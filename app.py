from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "4 es el antidoto del mundo mundial for ever y vladi es el crallador venenoso"})

if __name__ == "__main__":
    app.run(debug=True)
    
