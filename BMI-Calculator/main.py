#!/usr/bin/python3
"""This module calculates the Body Index Mass
    of any user
    It is calculated based on the unit the user decides on
    Units of lbs for weight and feet for height
    Units of Kg for weight and meter for height
"""


def bmi_calc():
    """Calculate BMI of a user"""
    print("Welcome to Body Mass Index(BMI) calculator")
    print("Choose a unit")
    unit = input("P for pounds/feet, K for Kilogram/meter: ")
    height_unit = float(input("Enter you height: "))
    weight_unit = float(input("Enter you weight: "))

    bmi = 0.0
    if unit == "P":
        bmi = 703 * (weight_unit / (height_unit * height_unit))
        print(bmi)
    elif unit == "K":
        bmi = weight_unit / (height_unit * height_unit)
        print(bmi)

    bmi = round(bmi, 2)

    if bmi < 18.5:
        print("Your BMI is {:.2f} and you are underweight".format(bmi))
    elif bmi > 18.5 and bmi <= 24.9:
        print("Your BMI is {:.2f} and it is at it's optimum".format(bmi))
    elif bmi > 24.9 and bmi <= 29.9:
        print("Your BMI is {:.2f} and you are are Overweight".format(bmi))
    elif bmi > 29.9 and bmi <= 34.9:
        print("Your BMI is {:.2f} and you are at Class 1 obesity".format(bmi))
    elif bmi > 34.9 and bmi <= 39.9:
        print("Your BMI is {:.2f} and you are at Class II obsesity".format(bmi))
    else:
        print("Your BMI is {:.2f} and you are at Class III obsesity".format(bmi))


if __name__ == "__main__":
    bmi_calc()
