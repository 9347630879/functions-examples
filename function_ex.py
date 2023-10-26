
#parameterless non returnable general function
def add():

    a = 100
    b = 200
    print( a + b)
add()

def sub():
    a = 100
    b = 200
    print( a - b)
sub()

def fib():
    n = 20
    a = 1
    b = 0
    i = 1
    while i<n:
        print(b)
        a = a + b
        b = a - b
        i = i + 1
fib()

def mul():
    a= 20
    b = 30
    print(a*b)
mul()
#parameterized function
def add(a:int  ,b:int ):


    print( a + b)
add(100,200)



def add(sai1:int , sai2:int ):
     print(sai1 + sai2)
def sub(sai1:int , sai2:int ):
    print(sai1 - sai2)

# add(10000,50000)
d = 55
k  = 66
sub(sai1=d , sai2=k)
sub(sai2=k , sai1=d)

def count():
    a = "saisundharaaaaaaaaa"
    print(a.count('a'))
count()


def append():
    lst =  []
    print(lst.append(''))
append()


def div(a,b):
    print(a/b)
div(100,200)
