# PC_price = 10000
# discount = 10  #% discount
# available_money = 9600

# print(available_money - PC_price*(100-discount) / 100 )

# print("nika's book")

# print(7 + 3)
# print(10 - 5)
# print(5 * 2)
# print(23 / 2)
# print(23 // 2)
# print(23 % 5)
# print(42 % 5)

#create variables from ages of your family members
#gamoitvalet ramdenjer aghemateba tqveni mamis asaki tqvens asaks 10 wlis shemdeg


# x = 7

# print(x != 8)
# print(x > 5)
# print(x < 2)
# print(x >= 7)
# print(x <= 7)

# print('a' > 'b')
 
# print("Bob" > "Dave")


# user_num = int(input("enter any number: "))
# #ojaxi
# if user_num >10:
#   print("მეტია 10-ზე")
# elif user_num ==10:
#   print("უდრის 10-ს")
# else:
#   print("ნაკლებია ათზე!")

#მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you

#მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you

# user_score1 = float(input("enter score N1: "))
# user_score2 = float(input("enter score N2: "))
# user_score3 = float(input("enter score N3: "))
# user_score4 = float(input("enter score N4: "))

# avg_score = (user_score1 + user_score2 + user_score3 + user_score4) / 4

# if avg_score>=9 and avg_score<=10:
#     print("გილოცავ, მატრიცელო. შენი ქულაა: " + str(avg_score) + " შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი, რასაც შეალიე შენი ცხოვრების წლები")
# elif avg_score <=5 and avg_score >= 0:
#      print("შენი ქულაა: " + str(avg_score) + " გილოცავ გაექეცი მატრიცას")
# elif avg_score >5 and avg_score <9:
#      print("შენი ქულაა: " + str(avg_score) + " YOU ARE MID")
# else:
#      print("შენი ქულაა: " + str(avg_score) + " there is something wrong with you")


# x = 42
# if x > 5:
#    print("x is greater than 5")
# elif x < 5:
#    print("x is less than 5")

###########################################

# limit = 18
# age = int(input("Sheiyvane sheni asaki: "))
# height = int(input("Sheiyvane sheni simagle: "))

# ###part1#####   ###part2#####
# if age > limit and height > 180:
#   print("Magalic Xar da Zrdasrulic")
# elif age > limit and height < 180:
#   print("zrdasruli xar tumca dabali")
# elif age < limit and height > 180:
#   print("Magali xar mara ar xar zrdasruli")
# else:
#   print("Vercerti kriteriumi ver daakmayofile!!!@@@")


  
# if not True:
#   print("1")
# elif not (1 + 1 == 3):
#   print("2")
# else:
#   print("3")

# marry = input("Will you marry me?")
# result = marry
# print (result)

# hour = 9
# day = 23
# print ((hour > 12 and day <= 15) or hour < 10)


#saiteracio cvladi (pudze iteracia (Iteration(განმეორება)))
# i = 1
# while i <=5:
#   print(i)
#   i = i + 1 #inkrementacia(ზრდა)

# print("Finished!")


#დავალება 1 - 30 ამდე დავპრინტოთ და დაგვიწეროს კენტია თუ ლუწია
#20 მუსიკის მოსმენა





from turtle import *
for i in range(4):
  forward(100)
  left(90)

penup()
goto(0, 200)
pendown()
for i in range(4):
  forward (100)
  left(90)

penup()
goto(-200, 200)
pendown()

for i in range(4):
  forward (100)
  left(90)

penup()
goto(-200, 0)
pendown()

for i in range(4):
  forward (100)
  left(90)

exitonclick()
