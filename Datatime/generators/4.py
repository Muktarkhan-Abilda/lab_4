def k(x,y):
    for i in range(x,y):
        yield i**2
x = int(input())
y = int(input())
for i in k(x,y):
    print(i, end =" ")