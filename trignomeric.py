import math

angle = float(input("Enter the angle in degrees: "))
rad = math.radians(angle)

sine_v = math.sin(rad)
cosine_v = math.cos(rad)
tangent_v = math.tan(rad)

print("The Sine is:", round(sine_v, 4))
print("The Cosine is:", round(cosine_v, 4))
print("The Tangent is:", round(tangent_v, 4))