from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")
    if name:
        return name.upper()
    return "Please provide name like ?name=yourname"

if __name__ == "__main__":
    app.run(debug=True)