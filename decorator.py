def greet(fun):
    def wrapper(name):
        print("hello")
        fun(name)
        print("good night")
    return wrapper



@greet
def sayname(name):
    print(name)
sayname("kht mite mite")