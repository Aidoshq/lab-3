import random

def gn():
    x=random.randint(1,20)
    print("Hello! What is your name?")
    name=str(input())
    print("Well, {}, I am thinking of a number between 1-20".format(name))
    cnt=0
    while True:
        print("Take a guess!")
        y=int(input())
        cnt+=1
        if y==x:
            print("Good job! you won in {} guesses".format(cnt))
            break
        elif y<x:
            print("it is too low")
        else:
            print("it is too high")
gn()