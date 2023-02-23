def foo(n):
    for i in range(len(n)):
        if n[i]==3 and n[i+1]==3:
            return True 
            break
    return False 

list = [int(i) for i in input().split()]
print(foo(list))