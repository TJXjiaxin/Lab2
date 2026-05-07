
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / height ** 2
    print("BMI = " + str(round(bmi, 2)))

    if bmi < 18.5:
        return -1
    elif bmi < 24.9:
        return 0
    else:
        return 1


result = calculate_bmi(weight=57, height=1.73)
print(result)