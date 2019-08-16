class Person:
    ''' class parameter name '''
    name = 'person'
    def __init__(self,name=None):
        '''instance parameter self.name'''
        self.name = name
n=Person('hai')
print('%s name %s'%(Person.name,n.name))
ni = Person()
ni.name = 'two'
print('%s name %s'%(Person.name,ni.name))
    
