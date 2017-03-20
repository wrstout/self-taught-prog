#write a program with a variable age assigned to an integer that prints different strings depending on what integer age is
age = 62
retirement = age - 65
print(retirement)
if age >=65:
    print("You're retired!")
elif retirement > -3:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")