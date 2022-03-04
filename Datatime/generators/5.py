def a(x):
    for i in range(x,0,-1):
        yield i

x = int(input())
for i in a(x):
    print(x,end = " ")