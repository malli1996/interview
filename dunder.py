class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
#double leading underscore we can access by reference variable and class name and variable
        self.__baz = 42
        self.__bam__ = 23
t2 = Test()
print(t2.foo)
print(t2._bar)
print(t2._Test__baz)
print(Test().__bam__)

#single trailing underscore
def make_object(name,class_):
    pass
