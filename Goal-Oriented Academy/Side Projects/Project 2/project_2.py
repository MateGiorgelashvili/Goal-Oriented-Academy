#Order System

Menu = ["Burger", "Pizza", "Nataxtari", "IceCream"]
Answers = ("No","Yes")
print(Menu)
food_option = input("Choose something from the menu: ")
food_option_2 = input("Anything else: ")
if food_option_2 == Answers[0]:
  print("Alright  Your order will be ready Soon!")
else:
  print("Your order will be ready Soon!")
