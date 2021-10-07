# basic pattern matching on tuples

x = (1,2) # declare a tuple

# extracting the components of x computationally
a = x[0]
b = x[1]
assert(a==1 and b==2)

# extracting the components of x with pattern matching
(p,q) = x
assert(p==1 and q==2)
