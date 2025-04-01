w = int(input("Weight (kg): "))
h = int(input("Height (cm): ")) / 100

print("\nLess than 18.5: Underweight")
print("18.5 - 24.9: Normal")
print("25 - 29.9: Overweight")
print("30 or more: Obese")

bmi = w / h ** 2
if w <=0 or h <= 0:
    print("Invalid input")
elif bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"\nBMI: {bmi:.2f} ({category})")