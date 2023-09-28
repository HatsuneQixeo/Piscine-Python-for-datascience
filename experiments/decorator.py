class Fak:
    att = "fak u"

    @classmethod
    # def classMethod(): # Error when called by either instance or type
    def classMethod(cls: type):
        print(cls.att)
        print("class method", type(cls))

    # def memberMethod(): # Error when called by instance, but not type
    def memberMethod(self: object):
        print(self.att)
        print("member method", type(self))

    @staticmethod
    def staticMethod():
        print("static method")

obj = Fak()

print("classmethod")
try:
    obj.classMethod()
    Fak.classMethod()
except Exception as e:
    print(f"{e.__class__.__name__}:", e)
print()

print("membermethod")
try:
    obj.memberMethod()
    # Fak.memberMethod(obj)
    Fak.memberMethod()
except Exception as e:
    print(f"{e.__class__.__name__}:", e)
print()

print("staticmethod")
try:
    obj.staticMethod()
    Fak.staticMethod()
except Exception as e:
    print(f"{e.__class__.__name__}:", e)
print()

f = Fak.staticMethod
f()
f = Fak.memberMethod
f(obj)
f = Fak.classMethod
f()
