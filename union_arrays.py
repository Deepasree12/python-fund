a=[1,2,3,4,5]
b=[6,7,8,9,10]
union=[]
for i in a:
    if i not in union:
        union.append(i)
        
for j in b:
    if j not in union:
           union.append(j)

union.sort()
print("union of arrays:",union)
            