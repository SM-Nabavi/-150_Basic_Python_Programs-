a = float(input("a: "))
b = float(input("b: "))

print("Before swapping")
print("a =", a)
print("b =", b)

# Swapping without a temporary variable 
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
 