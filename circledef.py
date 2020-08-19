def circle_area(x):
    num=x*x*3.14
    return num

def circle_circum(x):
    c=x*3.14
    return c


n = int(input('half'))
g = circle_area(n)
f = circle_circum(n)
print(g)
print(f)