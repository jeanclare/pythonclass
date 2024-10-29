#creae a program that checks a students perfomance

marks = int(input("Enter Marks"))

if 100 >= marks >= 80:
    print("You have an A")

elif 79 >= marks >= 60:
    print("You have an B")

elif marks <=59 and marks >=40:
    print("You have an C")

elif marks<=39 and marks >=0:
    print("You have an D")

else:
    print("Invalid Input")


#program that calculates the body mass index (BMI)

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Input: Weight in kilograms and height in meters
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Output BMI and Category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")