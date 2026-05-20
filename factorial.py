def fact(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact.__doc__)
print("the factorial of 0 is:", fact(0))
print("the factorial of 1 is:", fact(1))
print("the factorial of 2 is:", fact(2))
print("the factorial of 5 is:", fact(5))
print("the factorial of 10 is:", fact(10))