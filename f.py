def foo(s):
    a = s.split()
    a.reverse()
    x = ""
    for i in a:
        x+=i+" "
    return x

n = input()
print(foo(n))