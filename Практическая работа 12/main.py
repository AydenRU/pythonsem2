class Student:
    """Тут находится атрибуты класса"""
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        print(self.name)
        return self.name

    def getAge(self):
        print(self.age)
        return self.age

    def getGroupNumber(self):
        print(self.groupNumber)
        return self.groupNumber

    def SetNameAge(self, age):
        self.age = age

    def SetGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber



A = Student('A', 19, '1k')
A.getName()
A.getAge()
A.getGroupNumber()
A.SetNameAge(21)
A.SetGroupNumber('3k')
A.getAge()
A.getGroupNumber()

class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def A(self):
        self.a += self.b
        print(self.a)
        return self.a
    def M(self):
        self.a *= self.b
        print(self.a)
        return self.a
    def D(self):
        self.a = self.a / self.b
        print(self.a)
        return self.a
    def S(self):
        self.a -= self.b
        print(self.a)
        return self.a

A = Math(19, 5)
A.A()
A.M()
A.D()
A.S()


a = Student('Dima', 19, '1Курс')
print(Student.__doc__)

class Car():
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def On(self):
        print(f'Автомобиль заведен')
        return

    def Off(self):
        print(f'Автомобиль выключен')
        return

    def SetYear(self, year):
        self.year = year
        print(self.year)
        return

    def SetType(self, type):
        self.type = type
        print(self.type)
        return

    def SetColor(self, color):
        self.color = color
        print(self.color)
        return
A = Car('Синий', 'Тяжелая', '1994')
A.On()
A.Off()
A.SetYear('2021')
A.SetColor('Rad')
A.SetType('Lite')