def decor(outer_fun):
    def ifunc():
        print("hi,what's your name?")
        outer_fun()
        print("Nice to meet you")
        print("Let's go")
    return ifunc() #return keyword is optional.
@decor

def outer_fun():
    print("Hi,My name is \"Manikandan\"")
