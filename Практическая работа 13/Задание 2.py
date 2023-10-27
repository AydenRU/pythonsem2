class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        if len(s) == 0:
            return False
        else:
            return True

    def is_palindrom(self):
        if self.lower() == self[::-1].lower():
            return True
        else:
            return False

s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
p = SuperStr("123_321")
print(p.is_palindrom()) # True
