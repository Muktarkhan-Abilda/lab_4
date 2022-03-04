def a(n):
    for i in range(n):
        if i%2 == 0 and i!=0:
            yield i
n = int(input())
for x in a(n+1):
    if x == n or x == n - 1:
        print(x)
    else:
        print(x,end = ',')