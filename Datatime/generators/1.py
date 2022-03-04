def a(n):
    for i in range(n):
        yield i**2
n = int(input())
for x in a(n):
    print(x)