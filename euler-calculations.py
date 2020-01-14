def factorial(value):
    result=1
    for a in range(1, value+1):
        result=a*result
    return result

def euler_from_series(precission):
    result=0
    tmp=1
    while result<precission:
        result=1/factorial(tmp)
        tmp=tmp+1
    return result
print(euler_from_series(1/100000))