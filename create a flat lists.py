# create a flat lists
from functools import reduce
list=[[1,2],[3,4],[5,6]]
print(sum(list,[]))
print(reduce(lambda x,y = x+y, list))
