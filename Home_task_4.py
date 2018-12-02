def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result
result = factorial(100)
print(result)
