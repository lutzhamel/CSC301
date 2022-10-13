# program to demonstrate function dispatch tables

# functions to be put into the dispatch table
def good_morning(name):
   return ("Good morning, "+name+"!")

def good_afternoon(name):
   return ("Good afternoon, "+name+"!")

def good_evening(name):
   return ("Good evening, "+name+"!")

# create our dispatch table
myhash = dict()
myhash.update({"morning":good_morning})
myhash.update({"afternoon":good_afternoon})
myhash.update({"evening":good_evening})

# test out dispatch table
greeting_function = myhash["morning"]
assert(greeting_function("Joe") == "Good morning, Joe!")


