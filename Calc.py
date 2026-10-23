class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b

    def power(self, a, b):
        if a == 0 and b < 0:
            raise ValueError("Cannot raise zero to a negative power")
        return a ** b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
