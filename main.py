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
#Mathematical Formula to calculate
BMI=(weight_int/ height_float**2)
print(BMI)
BMI_INT = int(BMI)
print(BMI_INT)