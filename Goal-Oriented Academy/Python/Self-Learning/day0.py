# #Collection types

#######################################
#list -
#list = ["one", "two"]

#dictionary -
#dic = {1:"one", 2:"two"}

#tuple -
#tuple = ("one", "two")
#######################################



# #dictionaries

# ages = {
#    "Dave": 24,
#    "Mary": 42,
#    "John": 58,
#    "Mate": 15
# }

# print(ages["Dave"])
# print(ages["Mate"])

# #Dictionary Functions

# nums = {
#   1: "one",
#   2: "two",
#   3: "three",
# }
# print(1 in nums)
# print("three" in nums)
# print(4 not in nums)

#function get

# pairs = {
#    1: "apple",
#    "orange": [2, 3, 4], 
#    True: False, 
#    12: "True",
# }

# print(pairs.get("orange"))
# print(pairs.get(1, 412))
# print(pairs.get(12345, "not found"))
# print(len(pairs))

# person = {
#   "name": "mate",
#   "age": 15,
#   "Job": "Mini-Mentor",
#   "Academy": "GOA"
# }

# print(person.get("name", "not found"))
# print(person.get("age", "not found"))
# print(person.get("Job", "not found"))
# print(person.get("Academy", "not found"))
# print(person.get("Lover", "not found"))

##Tuples!!!!

# menu = ("eggs", "sausage", "chicken")
# print(menu[1])
# menu[1] = "robo" #ERROR

##Tuple unpacking

# numbers = (1, 2, 3)
# a, b, c= numbers
# a, b = b, a #swap values
# print(a)
# print(b)
# print(c)

# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(d)


##Sets!!
# num_set = {1, 2, 3, 4, 5}

# print(3 in num_set)

# nums = {1, 2, 1, 3, 1, 4, 5, 6}  #duplicate elements will  be removed
# print(nums)
# nums.add(-7)
# nums.remove(3)
# print(nums)

# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}

# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)


##List Comprehensions!!!!

# a list comprehension
# cubes = [i**3 for i in range(5)]

# print(cubes)

# evens=[i**2 for i in range(10) if i**2 % 2 == 0]

# print(evens)

##Summary!!!!

