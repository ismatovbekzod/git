n = int(input("son : "))
a1 = 0
a2 = 1
fib = 0
while fib <= n:
    a1 = a2
    a2 = fib
    fib =  a1+a2
print(a1)
print(a2+a1) 