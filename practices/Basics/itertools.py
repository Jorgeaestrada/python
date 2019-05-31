from itertools import product

a = {1,2}

print("range:")
print(range(3),a)
print("product > range:")
print(product(range(3),a))
print("list > product > range:")
print(list(product(range(3),a)))
print("len > list > product > range:")
print(len(list(product(range(3),a))))
