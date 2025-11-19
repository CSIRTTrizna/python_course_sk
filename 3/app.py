from flask import Flask, request


app = Flask(__name__)


@app.route("/sum", methods=['POST', 'GET'])
def summary():
    json_data = request.get_json(silent=True) or dict()
    arg = request.args
    numbers = json_data.get("numbers", arg.getlist("numbers")) or []
    return {"summary": sum([int(x) for x in numbers])}
