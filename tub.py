n = int(input("Son kiriting : "))
i = 2 
while i <= n:
    sanoq = 0
    for j in range(2,i+1):
        if i % j == 0:
            sanoq += 1
    if sanoq == 1:
        print(i,end=" ")
    i += 1
     