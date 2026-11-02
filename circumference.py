import math

print(f"value of Pi is: {math.pi:.2f}")
print(f"value of e is: {math.e:.2f}")
radius = float(input("Enter the radius of the circle: "))
circumference = 2*math.pi*radius
print(
    f"Circumference of the circle with radius {radius:.2f} is: {circumference:.02f}")
