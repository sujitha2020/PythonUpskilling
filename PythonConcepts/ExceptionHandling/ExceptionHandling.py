def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
    
    
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")