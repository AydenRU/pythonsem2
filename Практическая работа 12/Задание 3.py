class Car:
    def __init__(self, color='red' , type='lite', year='1999'):
        self.color = color
        self.type = type
        self.year = year

    def on(self):
        print('Автомобиль заведен')

    def off(self):
        print('Автомобиль заглушён')

    def setYear(self, year):
        self.year = year

    def setColor(self, color):
        self.color = color

    def setType(self, type):
        self.type = type

a = Car()
a.setType('heavy')
a.setYear('2005')
a.setColor('white')