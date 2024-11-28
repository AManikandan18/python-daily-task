##def create_multiplier(n):
##    return lambda x:x*n
##call=create_multiplier(5)
##print(call(8))

def create(x,y):
    return lambda x,y:x+y
call=create(5,5)
print(call(10,10))
