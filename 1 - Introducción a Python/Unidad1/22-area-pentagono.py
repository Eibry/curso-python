import math

side = float(input("¿Cuánto mide un lado del pentágono? "))

apothem = side / (2 * math.tan(math.radians(36)))
perimeter = side * 5
area = (perimeter * apothem) / 2

print("El área del pentágono es: " + str(round(area, 2)))