def fibanocci(n):
    list=[]
    for i in range(0,n):
       if i<=1:
           list.append(i)
       else:
           f=0
           f=list[-1]+list[-2]
           list.append(f)
           print(list)
           x=int(input("enter a limit"))
           fibanocci(x)
           