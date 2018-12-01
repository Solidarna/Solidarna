def largest_prime_factor(input_number):
    all_prime_factors = []
    for divider in range(2 ,input_number):
        if input_number % divider == 0:
            all_prime_factors.append(divider)
    return all_prime_factors


result = largest_prime_factor(100)
print(result)