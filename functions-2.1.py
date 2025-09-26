def areacalc(r):
    area = 3.141592658 * r * r
    return area

while True:
    radius = int(input("Input radius: "))
    calculation = areacalc(radius)
    print(calculation)