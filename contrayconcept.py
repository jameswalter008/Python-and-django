# file=open("writethetext.txt","w+")
# file.write("Hellofile. I am string.")
# file.seek(0)
# file.write("You ok my boi.")
# print(file.read())
# file.close()

#_________tuples________#
# tup=(1,'abc',2,'code')
# tup1=3,'efg',True
# tup2='A' #tup=('A',)
# tup=tup[0:4]+('A',)
# for x in ('a','b','c'):
#     print(x)

# def multipleresult():
#     return(1,2,'abc')
# print(multipleresult())

# list=[1,(2,3),'abc']
# list[len(list):]=[6]
# list.append(7)
# print(list)

#________list function_______#
# print(list(filter(lambda x:x<5,[1,2,3,4,5,6,7,8])))

# import functools
# print(functools.reduce(lambda x,y: x%y , [4,7]))
 
# print(list(map(lambda x: x,[1,2,3,4,5])))
# print(list(filter(lambda x: x<4,[1,2,3,4,5])))

#________dictionary_______#
# mydic={'key':'value','orange':2000}
# mydic['apple']=200
# # mydic.clear()
# print(mydic)


#________shallow copies_________#
# mydic={'Item' : 'Shirt', 'Size' : 'Medium', 'Price': 50}
# mydic1=mydic
# print(mydic)
# mydic['Size']='Small'
# print(mydic1)
# print(mydic)

#__________set___________#
# my_set=set(['two','three','one','one',])
# my_set1=set(['two','three','four','four'])
# a=my_set1 - my_set
# print(a)

#__________setfunc______#
# my_set=set(['two','three','one','one',])
# my_set1=set(['two','three','four','four'])
# print(set.union(my_set,my_set1))
# print(set.intersection(my_set1,my_set))
# print(set.difference(my_set1,my_set))


# def Isprime(n):
#     for x in range(2,int(n/2+1)):
#         if not n%x:
#             return False;
#     return True;
# def Primesto(n):
#     for x in range(2,n):
#         if Isprime(x):
#             print(x)
# Primesto(7)
# for x in range(2,2):
#     print(x)
 
# print(list(filter(lambda x: x<4, [1,2,3,4,5,6,7])))
import math
class complex:
    def __init__(self,real=0,imag=0):
        self.__real=real;
        self.__imag=imag;

    def getreal(self):
        return self.__real   

    def getimag(self):
        return self.__imag;

    def getmodule(self):
        return math.sqrt(self.getreal() * self.getreal() + self.getimag() * self.getimag())

    def Getphi(self):
        return math.atan2(self.getimag(),self.getreal())

    def setreal(self,value):
        if type(value) not in (int,float):
            raise Exception ('real part must be numbers')
        self.__real=value

    def setimag(self,value):
        self.__imag=value

c=complex(-3,4)
print(c.Getphi(),c.getmodule())