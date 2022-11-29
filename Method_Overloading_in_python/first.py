from multipledispatch import dispatch
#first it will take argument for two values
class overload:
    
    @dispatch(int,int)
    def sum(a,b):
        sum1 = a + b
        print(sum1)
    
#second it will take argument for third value
    @dispatch(int, int, float)
    def sum(a, b, c):
        sum2 = a+b+c
        print(sum2)
    

    
    