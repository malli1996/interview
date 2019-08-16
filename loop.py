#how to loop over a loop
mylist=[[1,2,3],[4,5,6,4],[7,8,9]]
print(mylist)
#for i in mylist:
 #   if len(i) == 3:
  #      print(i)
print([x for x in mylist if len(x) == 3 ])
