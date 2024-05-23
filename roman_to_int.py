"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""

roman = input("Enter Valid Roman Number: ")
total = 0
error = False

for i in roman:
    if (i == "I"):
        total += 1
    elif (i == "I"):
        total += 1
    elif (i == "V"):
        total += 5
    elif (i == "X"):
        total += 10
    elif (i == "L"):
        total += 50
    elif (i == "C"):
        total += 100
    elif (i == "D"):
        total += 500
    elif (i == "M"):
        total += 1000
    else:
        print("Syntax Error, Please enter valid roman number!")
        error = True
        break

if (error != True):

    before, after = "", ""
    for j in range(len(roman)):
        if (j != 0):
            before = roman[j - 1]
            after = roman[j]

            if (before == "I" and (after == "V" or after == "X")):
                total -= 2

            if (before == "X" and (after == "L" or after == "C")):
                total -= 20

            if (before == "C" and (after == "D" or after == "M")):
                total -= 200

    print(f"{roman} = {total}")
