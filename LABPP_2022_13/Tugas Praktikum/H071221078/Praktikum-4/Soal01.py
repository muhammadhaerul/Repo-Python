n = int(input())
def factorial(n):
    if n < 0:
        print("tidak terdefinisi")
    elif n > 1:
        return n * factorial(n-1)
    else:
        return 1
print(factorial(n))