def calculate_dcn(weight, height, age, gender, activity_level):
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please provide 'male' or 'female'.")

    activity_factors = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extremely active": 1.9
    }

    if activity_level.lower() in activity_factors:
        dcn = bmr * activity_factors[activity_level.lower()]
    else:
        raise ValueError("Invalid activity level.")

    return dcn

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ")
activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extremely active): ")

dcn = calculate_dcn(weight, height, age, gender, activity_level)
print("Your estimated daily calorie needs (DCN) is:", dcn)
