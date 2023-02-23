def foo(n):
    cnt = 0 
    for i in range(len(n)) :
        if (n[i] == 0) or (n[i]==7) :
            cnt+=1
    if cnt == 3:
        return True
    return False
    

spy = [input()]
print (foo(spy))