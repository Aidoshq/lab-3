import cmath 
def filter_prime(x):
    l = []
    for i in x:
        if i == 1 :
            continue
        if i == 2 : 
            l.append(2) 
            continue
        cnt = 0
        for j in range(2,i):
            if (i%j==0):
                cnt += 1
        if (cnt == 0):
            l.append(i)
    return l 
n = [int(i) for i in input().split()]
print (filter_prime(n))   