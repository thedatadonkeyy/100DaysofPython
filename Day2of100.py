#Data Types-converting string to integer

two_digit_number = input("Type a two digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result= int(first_digit) + int(second_digit)
print(result)

#Mathematical operations
print(3*3 + 3/3 -3) #PEMDAS
print(3 * (3+3) / 3-3 ) #PEMDAS

# BMI CALULATOR AS WHOLE NUMBER
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_int = int(weight)
height_float = float(height)
#Mathematical Formula to calculate BMI
BMI=(weight_int/ height_float**2)
print(BMI)
BMI_INT = int(BMI)
print(BMI_INT)

#rounding numbers
print(round(8/3))

# Calculate your life remaining in days, weeks, & months if you were to live 90 years
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
time_left=(90-int(age))
months = time_left*12
weeks = time_left*52
days = time_left*365
message = (f"You have {days} days, {weeks} weeks, and {months} months left.")

print(message)