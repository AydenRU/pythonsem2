class SuperStr(str):
    def __init__(self, s):
        self.s = s

    def is_repeatance(self, s):
        if type(s) == str:
            return True
        else:
            return False

    def is_palindrom(self):
        if self.s == "":
            return True
        else:
            s1 = ''
            for i in range(len(self.s)):
                i+=1
                s1 += self.s[-i]
            print(s1)
            if s1 == self.s:
                return True
            else:
                return False



s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True
