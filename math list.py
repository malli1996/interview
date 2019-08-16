#how to do math with lists
]cost=[1.20,30.33,40.78,40.34]
cases=[10,20,30,40]
for i in range(len(cost)):
    cost[i]=(cost[i]*cases[i]/sum(cases))
cost=sum(cost)
print(cost)
    
