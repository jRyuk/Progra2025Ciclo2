#0,1,1,2,3,5,8,13,21,34......
#n es hasta donde quiero llegar 

def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,n):
        siguiente= a + b
        a=b
        b= siguiente
        print(siguiente)

fibonacci(21)
