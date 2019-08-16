values = []
for p in range(1000,3001):
    x = str(p)
    if (int(x[0])%2==0) and (int(x[1])%2==0) and (int(x[2])%2==0) and (int(x[3])%2==0):
        values.append(x)
print(','.join(values))
2
