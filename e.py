import itertools
def foo(str):
    s = [''.join(i) for i in itertools.permutations(str)]
    for i in s:
        print (i,end=" ")
s = input()
foo(s)