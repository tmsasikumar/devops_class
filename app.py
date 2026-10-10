from flask import Flask, request

from src.logger import Logger
from src.utility import Utility

app = Flask(__name__)
logger = Logger("app")
utility = Utility(logger)


@app.route("/")
def hello():
    result = utility.division(request.args.get("a", 0), request.args.get("b", 0))
    if request.args.get("operation", "division") == "addition":
        result = utility.addition(request.args.get("a", 0), request.args.get("b", 0))
    elif request.args.get("operation", "division") == "division":
        result = utility.division(request.args.get("a", 0), request.args.get("b", 0))
    else:
        return "invalid operation", 400
    if isinstance(result, str):
        return result
    logger.info(f"result = {result}")
    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
