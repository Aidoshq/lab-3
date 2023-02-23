def foo(legs , heads):
    rabbit = legs/2-heads
    chick=heads-rabbit
    return [int(rabbit), int(chick)]

print(foo(35,94))
