# show that map will map any function onto a list
# here we map a greeting onto a list of names
# the result is a list of greetings

names = ["Joe","Bridget","Peter"]

def greeting(name):
   return "Hello "+name+"!"

greetings = list(map(greeting, names))
assert(greetings == ["Hello Joe!","Hello Bridget!","Hello Peter!"])

