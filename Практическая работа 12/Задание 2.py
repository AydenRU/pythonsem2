class Math:
    def __init__(self, a=float(), b=float()):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a // self.b

    def subtraction(self):
        return self.a - self.b


a = Math(12, 2)
print(f"Результат сложения: {a.addition()}\n")
print(f"Результат умножения: {a.multiplication()}\n")
print(f"Результат деления: {a.division()}\n")
print(f"Результат вычитания: {a.subtraction()}\n")