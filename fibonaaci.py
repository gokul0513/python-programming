def fibonaaci(k):
    if k==0:
        return 0
    elif k==1:
        return 1
    else:
        return fibonaaci(k-1)+fibonaaci(k-2)
for i in range(7):
    print(fibonaaci(i),end=" ")
        
        
