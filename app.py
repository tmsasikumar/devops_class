from flask import Flask, request

from logger import Logger

app = Flask(__name__)
logger = Logger("app")


@app.route("/")
def hello():
    a = float(request.args.get("a", 0))
    logger.info(f"a = {a}")
    b = float(request.args.get("b", 0))
    logger.info(f"b = {b}")
    result = a / b
    logger.info(f"result = {result}")
    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
