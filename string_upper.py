class InputOutput(object):
    def __init__(self):
        self.s = ''

    def getstring(self):
        self.s = input('enter a string:')
    def print(self):
        print(self.s.expandtab())
str = InputOutput()
str.getstring()
str.print()
