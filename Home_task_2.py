def the_product_of_abc(sum):
    for x in range(1, sum):
        for y in range(1, sum):
            z = sum - x - y
            if z ** 2 == x ** 2 - y ** 2:
                return x, y, z, x * y * z


result = the_product_of_abc(1000)
print(result)
