"""[LEARNING LOGS] Temperature"""
degree = float(input())
first_unit = input()
sec_unit = input()
if first_unit == sec_unit:
    print(degree)
else:
    if first_unit == "F":
        first_unit = (5*(degree-32))/9
    elif first_unit == "K":
        first_unit = degree-273.15
    elif first_unit == "R":
        first_unit = (degree-491.67)*(5/9)
    else:
        first_unit = degree

    if sec_unit == "K":
        print(f"{first_unit + 273.15:.2f}")
    elif sec_unit == "F":
        print(f"{((first_unit*9)/5)+32:.2f}")
    elif sec_unit == "R":
        print(f"{(first_unit*(9/5)+491.67):.2f}")
    else:
        print(f"{first_unit:.2f}")
