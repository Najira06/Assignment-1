year = int(input("Enter your year of birth: "))
datetime = 2023
age = datetime - year
print("Age is", age)
if age >=18:
    print ("You can vote")
else:
    print ("You can not vote")