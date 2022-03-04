def a(x):
    for i in range(x):
        if i%3 == 0 and i%4 == 0 and i!=0:
            yield i

x = int(input())
for i in a(x):
    print(i,end = " ")