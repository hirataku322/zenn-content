class test:
    def __init__(self):
        pass

    def __str__(self):
        return "test"


a = 1
b = "1"
c = test()
print(a, b, c)
print(repr(a), repr(b), repr(c))
print(id(a), id(b), id(c))
