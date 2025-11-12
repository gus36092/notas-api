from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Gustavo es el antídoto del mundo mundial for ever y Vladi es el creador venenoso"})

if __name__ == '__main__':
    app.run(debug=True)
