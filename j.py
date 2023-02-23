def foo(*num):
    a={}
    for i in num:
        if a.get(i) is not None:
            continue
        else:
            a[i]=True
    print(*a.keys())

foo(input())