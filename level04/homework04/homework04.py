# 1) 3 ცუდი პრაქტიკა ცვლადის დეკლარირების დროს:

# 2name = "Levan" #ცვლადის შექმნის დროს წინ რიცხვის დაწერა არ შეიძლება
# name1 = "Levan"

# your age = 23 # ცვლადის შექმნის დროს ადგილის გამოტოვება არ შეიძლება
# your_age = 23 

# his-name = "Nika"
# his_name = "Nika" # დეფისის გამოყენება არ შეიძლება ქვედა ტირის მაგივრად (SnakeCase)

# age -> 22 # მინიჭების ოპერატორის შეცვლა, გამოიყენება მხოლოდ "="- ტოლობის ნიშანი
# age = 22


# 2) Debugging (დებაგი) არის პროცესი, რომელიც მოიცავს იმ პრობლემის პოვნას და აღმოფქვრას, რომელმაც კომპიუტერულ პროგრამას გამართულად მუშაობაში ხელი შეუშალა!

# 3) Error-ები Python-ში:

SyntaxError	
TypeError	
IndexError	
KeyError	
AttributeError	
FileNotFoundError	
IndentationError	
NameError	
ValueError	
ZeroDivisionError
OverflowError


# 4) შეცდომების გასწორება
name = "Lika"
#print(namme)  მოვაშოროთ m
print(name)

number = "5"   # დავუმატოთ ""
text = " apples"
result = number + text
print(result)

#name = liKa  დავუმატოთ ბრჭყალები
name = "Lika"
name2 = name + "4"

first_user = "Lika"
   #2nduser = "Giorgi" # ცვლადის შექმნისას წინ რიცხვის დაწერა არ შეიძლება
second_user = "Giorgi"
print(first_user)

#first_name = "Data" # გამოვიყენით SnakeCase და სახელი ჩავსვით ბრჭყალებში
last_name = "random"

first_user = "Lika"
user2 = "Giorgi" # 2nduser შევცვალეთ user2-ით
print(first_user)


# 5)

city = input("Enter your city: ")
district = input("Enter your district: ")
building = input("Enter your building: ")
floor = input("Enter your floor: ")

print(f"I live in {city}, adress {district} {building} {floor}")

# 6)

age = input("Enter your age:")

print(f"You are {age} years old")

# 7)

num1 = input("Enter your num1:")
num2 = input("Enter your num2:")

print(num1 + num2)

# ბოლო მოქმედებაში თუ num1 = 3 და num2 = 7 ამ შემთხვევაში მათემატიკური მიმატების დროს ტერმინალში გამოგვიტანა 37 რადგან input-ში string ტიპის რიცხვებს აღიქვავს