from flask import Flask, request

from src.logger import Logger
from src.utility import Utility

app = Flask(__name__)
logger = Logger("app")
utility = Utility(logger)


@app.route("/")
def hello():
    operation = request.args.get("operation", "division")
    dict_operations = {
        "division": utility.division,
        "multiplication": utility.multiplication,
    }

    if operation not in dict_operations:
        return "invalid operation", 400

    result = dict_operations[operation](request.args.get("a", 0), request.args.get("b", 0))
    
    if isinstance(result, str):
        return result
    logger.info(f"result = {result}")
    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
