# global variable
name='aungkhantmoe'

def saymyname():
    # local
    global name
    name='aungaung'
    print(name)
saymyname();

print(name);