def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_obesity(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obesity Grade 1"
    elif bmi < 40:
        return "Obesity Grade 2"
    else:
        return "Obesity Grade 3"

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

result_bmi = calculate_bmi(weight, height)
classification = classify_obesity(result_bmi)

print("Your BMI is: {:.2f}".format(result_bmi))
print("Classification: ", classification)
