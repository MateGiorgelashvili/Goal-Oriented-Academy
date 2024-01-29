#SignUp System

Email = input("Enter your email: ")
Password = input("Enter your password: ")
Name = input("Enter your name: ")

print("You succesfully registered!")
print(f"Your email is: {Email} - Your password is: {Password} - Your Name is {Name}")

print("Please log-in to use New features!")
LogEmail = input("Enter your email: ")
LogPassword = input("Enter your password: ")
if LogEmail == Email and Password == LogPassword:
  print("You are ready to go!")
else:
  print("Email or Password is wrong!")
