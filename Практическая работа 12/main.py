class Student:
    def __int__(self, name='Ivan', age='18', groupNumber='10A'):
        self.name = name
        self.age = age
        self.gropNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getRoupeNumber(self):
        return self.gropNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.gropNumber = groupNumber

a1 = Student()
a1.setNameAge('Dima', '22')
a1.setGroupNumber('4 Курс')
print(f"Возраст учащегося {a1.getAge()}\n"\
      f"Имя студента {a1.getName()}\n"\
      f"Курс учащегося {a1.getRoupeNumber()}\n")
a2 = Student()
a2.setNameAge('Alina', '22')
a2.setGroupNumber('4 Курс')
print(f"Возраст учащегося {a2.getAge()}\n"\
      f"Имя студента {a2.getName()}\n"\
      f"Курс учащегося {a2.getRoupeNumber()}\n")
a3 = Student()
a3.setNameAge('Valia', '22')
a3.setGroupNumber('4 Курс')
print(f"Возраст учащегося {a3.getAge()}\n"\
      f"Имя студента {a3.getName()}\n"\
      f"Курс учащегося {a3.getRoupeNumber()}\n")
a4 = Student()
a4.setNameAge('Vlad', '22')
a4.setGroupNumber('4 Курс')
print(f"Возраст учащегося {a4.getAge()}\n"\
      f"Имя студента {a4.getName()}\n"\
      f"Курс учащегося {a4.getRoupeNumber()}\n")
