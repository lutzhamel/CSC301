from functools import reduce

x = 3

def mul(acc,j):
    return acc*j

fact = reduce(mul, [i for i in range(1,x+1)])

assert(fact == 6)
