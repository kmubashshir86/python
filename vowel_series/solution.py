def f(n):
    return int(64+((2*(n*n))+8*n-5+((-1)**n))/4)

for i in range(1,6):
         print(chr(f(i)))
