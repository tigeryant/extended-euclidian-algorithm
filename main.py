def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclid(b % a, a)
        return gcd, y - (b // a) * x, x

# a = 3 
# b = 5 
a = 99
b = 78
d, x, y = extended_euclid(a, b)
print(f"d: {d}, x = {x}, y = {y}")
print("d = gcd(a, b) = ax + by")
print(f"{d} = gcd({a}, {b}) = ({a} * {x}) + ({b} * {y})")
