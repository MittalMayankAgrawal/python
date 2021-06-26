def reverser_a_number(num):
    num=num/10
    return(num)

a=reverser_a_number(1234)
print(a)
# find the factorial of given no.
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
fact=factorial(5)
print(fact)

#program to find the maximum of three no. using function
def maximum(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3

a=maximum(2,3,5)
print(a)

            
