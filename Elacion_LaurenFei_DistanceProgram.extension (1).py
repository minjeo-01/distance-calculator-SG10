#input the given coordinates
import math
x1= float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#calculate the distance between the two given points
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#display the calculated result
print(f"The distance between the two points is: {distance:.2f}")
