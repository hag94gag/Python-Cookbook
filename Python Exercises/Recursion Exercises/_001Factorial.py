def factorial (num):
    print(f" start of the function {num}")
    if num==1:
        print(f"num is 1")
        return num
    else:
        print(f"before return {num}")
        return num*factorial(num-1)
    
# def factorial(n):
#   if(n==1):
#     return n
#   else:
#     return n*(factorial(n-1))



print(factorial(5))