def factorial(n):
    if n==1:
        return 1
    else:
        if n<0:
            print("이상한 숫자")
        else:
            return factorial(n-1)*n

print(factorial(5))
print(factorial(10))