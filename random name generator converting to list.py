import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
person_names = len(names)
a = random.randint(0, person_names - 1)
b = names[a]
print(b + " is going to buy a meal today.")
