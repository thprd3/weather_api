from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "tjeneste": "vaer-api"})

if __name__ == "__main__":
    app.run()
