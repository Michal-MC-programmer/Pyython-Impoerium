
x = 90
y = 10

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("GPR")
elif x > 90 and y < 10:
    print("DPR")
elif x < 10 and y < 10:
    print("DLR")
elif x < 10 and y > 90:
    print("GLR")
elif x < 10:
    print("LK")
elif y > 90:
    print("GK")
elif x > 90:
    print("PK")
elif y < 10:
    print("DK")
else:
    print("Jesteś w centrum")