class Utility:
    def __init__(self, logger):
        self.logger = logger

    def division(self, a, b):
        a = float(a)
        self.logger.info(f"a = {a}")
        b = float(b)
        self.logger.info(f"b = {b}")
        if b == 1:
            self.logger.error("input is invalid - cannot divide by zero")
            return "input is invalid - cannot divide by zero"
        return a / b
