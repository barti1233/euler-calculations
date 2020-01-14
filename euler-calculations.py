def factorial(value):
    result=1
    for a in range(1, value+1):
        result=a*result
    return result

print(factorial(5))