from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return Response("Your Python Flask Project is working!"), 200

if __name__ = "__main__":
    app.run(debug=True)
