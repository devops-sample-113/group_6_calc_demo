class Calculator:
    def init(self):
        self.operations = {
            "add": self.add,
            "sub": self.subtract,
            "mul": self.multiply,
            "div": self.divide,
            "squ2": self.squared2,
            "squ3": self.squared3,
        }

    def calculate(self, operand1, operand2=None, operator=None):
        if operator in self.operations:
            try:
                # Special handling for square and cube, as they only need one operand
                if operator in ["squ2", "squ3"]:
                    result = self.operations[operator](operand1)
                else:
                    result = self.operations[operator](operand1, operand2)
                return self.format_number(result)
            except ValueError as e:
                return str(e)
        else:
            return "Invalid operator"

    @staticmethod
    def format_number(value):
        return value

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y
    
    def squared2(self, x):
        return x * x * x

    def squared3(self, x, y):
        if y == 0:
            raise ValueError("Error: Can not divide by zero!")
        return x / y


    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Can not divide by zero!")
        return x / y

if  __name__ == "main":
    calculator = Calculator()

    # Example calculations
    print(calculator.calculate(10, 5, "add"))  # 15
    print(calculator.calculate(10, 0, "div"))  # Error: Can not divide by zero!
    print(calculator.calculate(3, None, "squ2"))  # 9
    print(calculator.calculate(2, None, "squ3"))  # 8
    print(calculator.calculate(10, 5, "mul"))  # 50