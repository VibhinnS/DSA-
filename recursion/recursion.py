def fibo(number):
    if number < 2:
        return number
    else:
        return fibo(number-1) + fibo(number-2)


print(fibo(4))
