# 1) type() ფუნქცია - Python-ში type() ფუნქცია გამოიყენება ობიექტის მონაცემთა ტიპის (მაგ. int, str, list) დასადგენად.
num1 = 12
num2 = 0.1
num3 = '3'
user_name = 'Levan'

print(type(num1))
print(type(num2))
print(type(num3))
print(type(user_name))
print(type(True))

#2) ეცადეთ გამოიტანოთ წინადადება "I am NAME SURNAME and i am YEARS years old" კონკატინაციით
name = 'Levan'
surname = 'Kobaidze'
age = 28

print("I am " + name + " " + surname + " and I am " + str(age) + " years old") # age- სტრინგად იმიტომ ვაქციეთ რომ ინტეჯერსა და სტრინგს შორის მათემატიკურ მოქმედებას ვერ შევასრულებთ

# 3) ათწილადები

n1 = float(input('enter your first number: '))
n2 = float(input('enter your second number: '))
addition = n1 + n2
deduction = n1 - n2
multiply = n1 * n2
division = n1 / n2

print(addition)
print(deduction)
print(multiply)
print(division)


# 4)
a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))
d = int(input('enter fourth number: '))
e = int(input('enter fifth number: '))

arithmetical_average = (a + b + c + d + e) /5
print(arithmetical_average)

# 5) convert celsius to fahrenheit

celsius = float(input('enter temperature in celsius: '))
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)

# 6) convert fahrenheit to celsius

fahrenheit = float(input('enter temperature in fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8
print(celsius)


