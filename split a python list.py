#How to split a python list
x=[1,2,3,4,5,6,7,8,9]
y=zip(*[iter(x)]*3)
print(list(y))
