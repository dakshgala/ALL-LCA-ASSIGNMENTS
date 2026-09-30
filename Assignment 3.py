# Assignment 3: Check whether a triangle is right-angled (using a function)

def is_right_angled(a, b, c):
    """Return True if sides a, b, c form a right-angled triangle."""
    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Sort so the longest side is treated as the hypotenuse
    x, y, z = sorted([a, b, c])
    # Must be a valid triangle (sum of two smaller sides > largest side)
    if x + y <= z:
        return False
    # Pythagoras theorem: x^2 + y^2 = z^2
    return x ** 2 + y ** 2 == z ** 2


side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

if is_right_angled(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is NOT a right-angled triangle.")
