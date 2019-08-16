def foo(l):
    l[1] = l[1] * 100
    print(id(l))
    return l
mylist = [1,2,3]
print (id(mylist))
a = foo(mylist)
print(a)
