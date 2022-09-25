
# ? -------------------------------------------------------------------------------------------- EX 018-001
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# name = "Omar "
# age = "22 "
# country = "Cario "

# print("My Name Is",name)
# print("My Age IS",age)
# print("My Country IS",country)
# print("My Name Is {0}\nMy Age Is {1}\nMy Country Is {2}".format(
#     name, age, country))
# print(f"My Name IS {name}\nMy Age IS {age}\nMY Country {country}")
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# output="Hello, My Name Is {0}And Iam {1}Years Old and I Live in {2}.".format(name,age,country)
# output1="Hello, My Name Is " +name+"And Iam "+age+"Years Old and I live in "+country+"."
# output2=f"Hello, My Name Is {name}And Iam {age}Years Old and I Live in {country}."
# print(output)
# print(output1)
# print(output2)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# name = "Omar "
# age = "22 "
# country = "Cario "
# print(type(name))
# print(type(age))
# print(type(country))
# ? -------------------------------------------------------------------------------------------- EX 018-011
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# name = "Osama"
# age = "38"
# country = "Egypt"
# print("\"Hello "+"'"+name+"'"+", " +
#       "How You Doing \\ \"\"\" Your Age Is \""+age+"\"\" + And Your Country Is: "+country)

# print(f"\"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

# print("\"Hello '{0}', How You Doing \\ \"\"\" Your Age Is \"{1}\"\" + And Your Country Is: {2}".format(name, age, country))
# print(
#     "\"Hello \'{0:s}\', How You Doing \\ \"\"\" Your Age Is \"{1:d}\"\" + And Your Country Is : {2:s}".format(name, age, country))
# print(
# "\"Hello \'{n:s}\', How You Doing \\ \"\"\" Your Age Is \"{a:d}\"\" + And Your Country Is : {Country:s}".format(n="Omar", a=22, Country="Egypt"))

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# name = "Osama"
# age = "38"
# country = "Egypt"
# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt
# print("\"Hello \'"+name+"' , How You Doing \\\
# \n\"\"\" Your Age Is \""+age+"\"\" + \
# \nAnd Your Country Is: "+country)

# myStringSix = """First
# Second "Test" \\\ 'Test'
# Third"""  # لكتابه اكتر من سطر نستخدم 3 دابل كوت في الاول والاخر
# print(myStringSix)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# name = 'Elzero'
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
# print(name[1])
# print(name[-5])
# print(name[2])
# print(name[-4])
# print(name[5])
# print(name[-1])
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# name = 'Elzero'

# print(name[1]+name[2]+name[3]) # lze"
# print(name[0]+name[2]+name[4])  # "Ezr"
# print(name[4]+name[2]+name[0])  # "rzE"

# print(name[1:4]) # lze"
# print(name[::2]) #"Ezr"
# print(name[4::-2]) #"rzE"
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# name = "#@#@Elzero#@#@"
# print(name.strip("#@"))
# print(name.replace("#@",""))
# >---------------------------------------
# ^^ Assign 6
# >---------------------------------------
# num = "9"
# num1 = "15"
# num2 = "130"
# num3 = "950"
# num4 = "1500"

# print(num.zfill(4))
# print(num1.zfill(4))
# print(num2.zfill(4))
# print(num3.zfill(4))
# print(num4.zfill(4))
# >---------------------------------------
# ^^ Assign 7
# >---------------------------------------
# name_one = "Osama"
# name_two = "Osama_Elzero"

# $$$$$$$$$$$$$$$Osama
# $$$$$$$$Osama_Elzero
# print(name_one.rjust(20,"$"))
# print(name_two.rjust(20,"$"))
# >---------------------------------------
# ^^ Assign 8
# >---------------------------------------
# name_one = "OSamA"
# name_two = "osaMA"

# print(name_one.swapcase())# osAMa
# print(name_two.swapcase())# OSAma
# >---------------------------------------
# ^^ Assign 9
# >---------------------------------------
# msg = "I Love Python And Although Love Elzero Web School"

# print(msg.count("Love"))# 2
# >---------------------------------------
# ^^ Assign 10
# >---------------------------------------
# name = "Elzero"

# print(name.index("z")) # 2
# print(name.find("z")) # 2
# >---------------------------------------
# ^^ Assign 11
# >---------------------------------------
# msg = "I <3 Python And Although <3 Elzero Web School"

# I Love Python And Although <3 Elzero Web School
# print(msg.replace("<3", "Love", 1))
# >---------------------------------------
# ^^ Assign 12
# >---------------------------------------
# msg = "I <3 Python And Although <3 Elzero Web School"

# I Love Python And Although Love Elzero Web School
# print(msg.replace("<3", "Love"))
# >---------------------------------------
# ^^ Assign 13
# >---------------------------------------
# name = "Osama"
# age = 38
# country = "Egypt"

# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
# print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
# print("MY Name Is {0:s}, And My Name Is {1:d}, And My Country Is {2:s}".format(
#     name, age, country))
# ? -------------------------------------------------------------------------------------------- EX 020-019
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# print(type(10))
# print(type(10.2))
# print(type(8+1j))
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# complexnum = 1+2j

# print("Imaginary Part Is: {}".format(complexnum.imag))  # Imaginary Part
# print("Real Part Is: {}".format(complexnum.real))  # Real Part
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# num = 10
# num1 = "10"
# x = num1.replace("10", "10.0000000000")

# print("{:.10f}".format(num))
# print("{:.10f}".format(float(num)))
# print(x)
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# num = 159.650

# print(int(num)) # 159
# print(type(int(num))) # <class 'int'>
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# print(100 - 115) # = -15
# print(50 * 30 ) #= 1500
# print(21 % 4 ) #= 1
# print(110 // 11 ) #= 10
# print(int(97 / 20)) #= 4
# ? -------------------------------------------------------------------------------------------- EX 023-021
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[0])# "Osama" => Method One
# print(friends[-5])
# print(friends.pop(0))# "Osama" => Method Two
# print(friends[-1])  # "Mahmoud" => Method One
# print(friends[4])  # "Mahmoud" => Method Two
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[::2])  # "Osama", "Sayed", "Mahmoud"
# print(friends[1:4:2])# "Ahmed", "Ali"
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(f"{friends[1:4]}")  # "Ahmed", "Sayed", "Ali",
# print("{0}".format(friends[1:4]))  # "Ahmed", "Sayed", "Ali",
# print(friends[1:4])  # "Ahmed", "Sayed", "Ali",
# print(friends[-4:4])  # "Ahmed", "Sayed", "Ali",
# print(friends.pop(1)+" "+friends.pop(1)+" " +friends.pop(1))  # "Ahmed", "Sayed", "Ali",
# print(friends[1:4:1])  # "Ahmed", "Sayed", "Ali",

# print(friends[-2:])# "Ali", "Mahmoud"
# print(friends[3:])# "Ali", "Mahmoud"
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# friends[3]="Elzero"
# friends[4]="Elzero"
# print(friends)
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# friends = ["Osama", "Ahmed", "Sayed"]

# friends.insert(0, "Nasser")
# print(friends)
# friends.append("Salem")
# print(friends)
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# >---------------------------------------
# ^^ Assign 6
# >---------------------------------------
# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# friends.remove("Nasser")
# print(friends)
# friends.remove("Salem")
# print(friends)
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
# >---------------------------------------
# ^^ Assign 7
# >---------------------------------------
# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends)
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# >---------------------------------------
# ^^ Assign 8
# >---------------------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# friends.sort()
# print(friends)# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# friends.sort(reverse=True)
# print(friends)# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
# >---------------------------------------
# ^^ Assign 9
# >---------------------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# print(len(friends))# 6
# >---------------------------------------
# ^^ Assign 10
# >---------------------------------------
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# print(technologies[-1][0])  # Django
# print(technologies[-1][2])  # Web
# ? -------------------------------------------------------------------------------------------- EX 025-024
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# names="Bashing",
# print(names[0])
# print(type(names))
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# friends = ("Osama", "Ahmed", "Sayed")

# print(f"{friends}".replace("Osama", "Elzero"))# ("Elzero", "Ahmed", "Sayed")
# print(type(friends))# <class 'tuple'>
# print(len(friends))# 3 Elements
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# nums = (1, 2, 3)
# letters = ("A", "B", "C")

# nums_and_letters_one=nums+letters
# print(nums_and_letters_one) #(1, 2, 3, "A", "B", "C")
# print(len(nums_and_letters_one)) # 6 Elements
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# my_tuple = (1, 2, 3, 4)

# print(my_tuple[0]) # 1
# print(my_tuple[1]) # 2
# print(my_tuple[-1]) # 4
# ? -------------------------------------------------------------------------------------------- EX 032-026
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# my_list = [1, 2, 3, 3, 4, 5, 1]

# my_list.remove(3)
# unique_list = my_list[:5]
# print(unique_list)
# print(type(unique_list))  # <class 'list'>
# unique_list.remove(5)
# print(unique_list)# 1, 2, 3, 4
# >-------------------
# unique_list = my_list[:3]+my_list[4:6]
# print(unique_list)  # 1, 2, 3, 4, 5
# print(type(unique_list))  # <class 'list'>
# print(unique_list[:4])# 1, 2, 3, 4
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# nums.symmetric_difference_update(letters)
# print(nums)  # {1, 2, 3, "A", "B", "C"}
# print(nums | letters) # {1, 2, 3, "A", "B", "C"}
# print(nums.union(letters))  # {1, 2, 3, "A", "B", "C"}
# nums.update(letters)
# print(nums)  # {1, 2, 3, "A", "B", "C"}
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set)  # {1, 2, 3}
# my_set.clear()
# print(my_set)  # set()
# my_set.add("A")
# my_set.add("B")
# my_set.discard("C")
# print(my_set)#{"A", "B"}
# >------------
# print(my_set)  # {1, 2, 3}
# my_set.clear()
# print(my_set)  # set()
# my_set.update(letters)
# my_set.remove("C")
# print(my_set)# {"A", "B"}
# my_set.discard("C")
# print(my_set)
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_two.issuperset(set_one))# True
# print(set_one.issubset(set_two))# True
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# diCover = {"prog1": "HTML",
#            "progress1": "90%",
#            "prog2": "CSS",
#            "progress2": "90%",
#            "prog3": "Python",
#            "progress3": "80%"
#            }
# "HTML Progress Is 90%"
# print(f"{diCover['prog1']} Progress Is {diCover['progress1']}")
# "CSS Progress Is 80%"
# print(f"{diCover['prog2']} Progress Is {diCover['progress2']}")
# "Python Progress Is 80%"
# print(f"{diCover['prog3']} Progress Is {diCover['progress3']}")
# diCover.update({'prog4': 'AI', "progress4": '20%'})
# "Python Progress Is 80%"
# print(f"{diCover['prog4']} Progress Is {diCover['progress4']}")
# "AI Progress Is 20%"
# ? -------------------------------------------------------------------------------------------- EX 037-033
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# print(bool("Osama"))  # True
# print(bool(100))  # True
# print(bool(100.95))  # True
# print(bool(True))  # True
# print(bool([1, 2, 3, 4, 5]))  # True
# print(bool(10 > 5))  # True

# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(5 > 10))  # False
# print(bool([]))  # False
# print(bool(None))  # False
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# html = 80
# css = 60
# javascript = 70

# print(html > 50 and css > 50 and javascript > 50)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# num_one = 10
# num_two = 20
# num = 20

# print(num > num_one or num < num_two) # True
# print(num > num_one and num < num_two) # False
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# num_one = 10
# num_two = 20

# result = num_one+num_two
# print(result)  # 30
# print(result**3)  # 27000
# print("{:.0f}".format(result**3/27))  # 1000
# print(result**3/27/5)# 200.0
# print(type(str(result**3/27/5)))# <class 'str'>
# ? -------------------------------------------------------------------------------------------- EX 040-038
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# name = input('Type Your Name : ').strip().capitalize()

# print(f"Hello {name}, Happy To See You Here.")
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# age = int(input("Type Your Age : ".strip()))

# age < 16 == print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# age >= 16 == print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# first_name = input("Tyep Your First Name : ").strip().capitalize()
# second_name = input("Tyep Your Second Name : ").strip().capitalize()

# print("Hello {0} {1:.1s}.".format(first_name, second_name))
# print(f"Hello {first_name} {second_name:.1s}.")  # Example "Omar A."
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# email=input("Type Your email : ").strip().lower()

# "Osama@Nn.Sa" # Email

# uName=email[:email.index("@")].capitalize()
# theEmail = email[email.index("@")+1:-4]
# tagMali=email[email.index("@")+1:email.index(".")]
# dominMail=email[email.index(".")+1:]
# print(f'Your Name Is {uName}')
# print(f'Email Service Provider Is {theEmail}')
# print(f'Email Service Provider Is {tagMali}')
# print(f'Top Level Domain Is {dominMail}')
# ? -------------------------------------------------------------------------------------------- EX 046-041
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# num1 = int(input("Type First Number : ").strip())
# num2 = int(input("Type Second Number : ").strip())

# operation = input("Choose Any Operation + or - or * or / or % : ").strip()

# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)
# elif operation == "%":
#     print(num1 % num2)
# else:
#     print("Plase Choose Any Operation (+ Or - Or * Or / Or % )")
# >----------------------------------------
# if operation == "+":
#     print(f"{num1} + {num2} =", num1 + num2)
# elif operation == "-":
#     print(f"{num1} - {num2} =", num1 - num2)
# elif operation == "*":
#     print(f"{num1} * {num2} =", num1 * num2)
# elif operation == "/":
#     print(f"{num1} / {num2} =", num1 / num2)
# elif operation == "%":
#     print(f"{num1} % {num2} =", num1 % num2)
# else:
#     print("Plase Choose Any Operation (+ Or - Or * Or / Or % )")
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# age = 16

# print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# uAge = int(input("Type You Age : ").strip())
# if uAge >= 10 and uAge <= 100:
#     month = uAge * 12
#     print(f"Your Age In Months => \"{month:,}\" Months.")
#     weeks = month * 4
#     print(f"Your Age In Months => \"{weeks:,}\" Weeks.")
#     days = weeks * 365
#     print(f"Your Age In Months => \"{days:,}\" Days.")
#     hours = days * 24
#     print(f"Your Age In Months => \"{hours:,}\" Hours.")
#     minute = hours * 60
#     print(f"Your Age In Months => \"{minute:,}\" Minutes.")
#     seconds = minute * 60
#     print(f"Your Age In Months => \"{seconds:,}\" Seconds.")
# else:
#     print("You Are Age Is OutZone Go Back")
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# country = input("Type Your Country For Discount : ").capitalize().strip()
# countries = ["Egypt", "Palestine", "Syria",
#              "Yemen", "Ksa", "Usa", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countries:
#     print(
#         f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
# else:
#     print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# ? -------------------------------------------------------------------------------------------- EX 050-047
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# num = int(input("Type Number : ").strip())
# numS = num-1
# if num > 0:
#     while num > 1:
#         print(f"{num-1}")
#         num -= 1
#     else:
#         print(f"{numS} Numbers Printed Successfully.")
# else:
#     print(f"Number {1+numS} Is Not Larger Than 0")
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# minLen = 0
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# frino = []
# while len(friends) > minLen:
#     if friends[minLen].capitalize() in friends:
#         print(friends[minLen])
#         minLen += 1
#         continue
#     if friends[minLen].lower() in friends:
#         frino.append(friends[minLen].lower())
#         minLen += 1
#         frino.append(friends[minLen].lower())
#         friends.remove(friends[minLen].lower())

# print(f"Friends Printed And Ignored Names Count Is {len(frino)} Your List Is => {frino}")
# # >---------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print(f"{skills[0]}\n{skills[1]}\n{skills[2]}\n{skills[3]}\n{skills[4]}");break
# while skills:
#     print(f"{skills[:]}");break
# # >---------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# my_friends = []
# maximumppl = 4
# while maximumppl > 0:
#     name_Add = input("Type Your Name : ").strip()
#     if name_Add.isupper():
#         print("Invalid Name")
#     elif name_Add.islower():
#         my_friends.append(name_Add.strip().capitalize())
#         maximumppl -= 1
#         print(
#             f"Friend {name_Add.capitalize()} Added => {len(my_friends)}st Letter Become Capital")
#         print(f"Names Left in List Is {maximumppl}")
#         print(my_friends)
#     elif name_Add.capitalize():
#         my_friends.append(name_Add.strip())
#         maximumppl -= 1
#         print(f"Friend {name_Add} Added => {len(my_friends)}st Letter Become Capital")
#         print(f"Names Left in List Is {maximumppl}")
#     else:
#         print("Invalid Name Plase Type You Name First Letter Is Capital")
# if len(my_friends) > 0:

#  my_friends.sort()

# index = 0

# while index < len(my_friends):

#     print(my_friends[index])

#     index += 1
# print(my_friends)
# >-----------------------------------------
# my_friends = []
# maximumppl = 4
# while maximumppl > 0:
#     pplName = input("Type Your Name To Add : ").strip()
#     if pplName == pplName.upper():
#         print("Invalid Name")
#     elif pplName == pplName.lower():
#         my_friends.append(pplName.strip().capitalize())
#         maximumppl -= 1
#         print(
#             f"Friend {pplName.capitalize()} Added => {len(my_friends)}st Letter Become Capital")
#         print(f"Names Left in List Is {maximumppl}")
#         print(my_friends)
#     elif pplName == pplName.capitalize():
#         my_friends.append(pplName.strip())
#         maximumppl -= 1
#         print(f"Friend {pplName} Added")
#         print(f"Names Left in List Is {maximumppl}")
#     else:
#         print("Invalid Name Plase Type You Name First Letter Is Capital")

# if len(my_friends) > 0:

#  my_friends.sort()

# index = 0

# while index < len(my_friends):

#     print(my_friends[index])

#     index += 1
# print(my_friends)
# ? -------------------------------------------------------------------------------------------- EX 055-051
# # >---------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# my_nums.sort(reverse=True)
# for nums in my_nums:
#     # print(nums)
#     if nums % 5 == 0:
#         print(nums)
#         pass
# else:
#     print("All Numbers Print Sussfully")
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# nums=range(1,21)
# for a in nums:
#     if a == 6 or a == 8 or a== 12:
#         continue
#     print(f"{a}".zfill(2))
# else:
#     print("Loop Is Sussfully")
# ?-------------------------------------------
# mynums = range(1, 21)
# for numes in mynums:
#     if numes == 6:
#         continue
#     # print(f"{numes}".zfill(2))
#     elif numes == 8:
#      continue
#     # print(f"{numes}".zfill(2))
#     elif numes == 12:
#      continue
#     print(f"{numes}".zfill(2))
# else:
#     print("Loop Is Sussfully")
# # >---------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# abc=[]
# for rank in my_ranks:
#     A, B, C = 100, 80, 40
#     if rank == "Math":
#         print(f"My Rank in {rank} Is A And This Equal {A} Points")
#         abc.append(A)
#     if rank == "Science":
#         print(f"My Rank in {rank} Is A And This Equal {B} Points")
#         abc.append(B)
#     if rank == "Drawing":
#         print(f"My Rank in {rank} Is A And This Equal {A} Points")
#         abc.append(A)
#     if rank == "Sports":
#         print(f"My Rank in {rank} Is A And This Equal {C} Points")
#         abc.append(C)
# else:print(f"Total Points Is {abc[0]+abc[1]+abc[2]+abc[3]}")
# ?----------------------------------------------------------
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# abc = []
# for rank in my_ranks:
#     A, B, C = 100, 80, 40
#     if "A" in my_ranks[rank]:
#         print(
#             f"My Rank in {rank} Is ( {my_ranks[rank]} ) And This Equal {A} Points")
#         abc.append(A)
#     if my_ranks[rank] == "B":
#         print(
#             f"My Rank in {rank} Is ( {my_ranks[rank]} ) And This Equal {B} Points")
#         abc.append(B)
#     if my_ranks[rank] == "C":
#         print(
#             f"My Rank in {rank} Is ( {my_ranks[rank]} ) And This Equal {C} Points")
#         abc.append(C)
# else:
#     print(f"Total Points Is {abc[0]+abc[1]+abc[2]+abc[3]}")
# ?----------------------------------------------------------
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# abc=[]
# for ranks in my_ranks:
#     A, B, C = 100, 80, 40
#     if my_ranks[ranks] == "A":
#         print(
#             f"My Rank in {ranks} Is {my_ranks[ranks]} And This Equal {A} Points")
#         abc.append(A)
#     elif my_ranks[ranks] == "B":
#         print(
#             f"My Rank in {ranks} Is {my_ranks[ranks]} And This Equal {B} Points")
#         abc.append(B)
#     elif my_ranks[ranks] == "C":
#         print(
#             f"My Rank in {ranks} Is {my_ranks[ranks]} And This Equal {C} Points")
#         abc.append(C)
# else:
#     print(f"Total Points Is {abc[0]+abc[1]+abc[2]+abc[3]}")
#     print(f"Total Points Is {abc.pop(0)+abc.pop(0)+abc.pop(0)+abc.pop(0)}")
# # >---------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }
# A, B, C, D = 100, 80, 40, 20
# abcd = []
# for student in students:
#     print("------------------------------")
#     print(f"Student Name => {student}")
#     print("------------------------------")
#     for std_key, std_value in students[student].items():
#         if "A" in std_value:
#             print(f"{std_key} => {A}")
#             abcd.append(A)
#         elif "B" in std_value:
#             print(f"{std_key} => {B}")
#             abcd.append(B)
#         elif "C" in std_value:
#             print(f"{std_key} => {C}")
#             abcd.append(C)
#         elif "D" in std_value:
#             print(f"{std_key} => {D}")
#             abcd.append(D)
#     print(
#         f"Total Points For {student} Is {abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)}")
# !                                  outPut
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
# "------------------------------"
# "-- Student Name => Sayed"
# "------------------------------"
# "- Math => 80 Points"
# "- Science => 80 Points"
# "- Draw => 80 Points"
# "- Sports => 20 Points"
# "- Thinking => 100 Points"
# "Total Points For Sayed Is 360"
# "------------------------------"
# "-- Student Name => Mahmoud"
# "------------------------------"
# "- Math => 20 Points"
# "- Science => 100 Points"
# "- Draw => 100 Points"
# "- Sports => 80 Points"
# "- Thinking => 80 Points"
# "Total Points For Mahmoud Is 380"
# ?------------------------------
# for student in students:
#     print("------------------------------")
#     print(f"Student Name => {student}")
#     print("------------------------------")
#     for std_key in students[student]:
#       for std_value in students[student][std_key]:
#         if "A" in std_value:
#             print(f"{std_key} => {A}")
#             abcd.append(A)
#         elif "B" in std_value:
#             print(f"{std_key} => {B}")
#             abcd.append(B)
#         elif "C" in std_value:
#             print(f"{std_key} => {C}")
#             abcd.append(C)
#         elif "D" in std_value:
#             print(f"{std_key} => {D}")
#             abcd.append(D)
#     print(
#         f"Total Points For {student} Is ( {abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)} )")
# ? -------------------------------------------------------------------------------------------- EX 059-056
# # >---------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# def calculate(num1, num2, operation="add"):
#     if operation in ["a", "add", 'AdD', "A"]:
#         print(num1+num2)
#     elif operation in ["S", "subTRACT", "subtract", "s"]:
#         print(num1-num2)
#     elif operation in ["m", "multiply", "Multiply", "M"]:
#         print(num1*num2)

# calculate(10, 20, "m")
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# def addition(*Parameters):
#     sums = 0
#     for num in Parameters:
#         if num == 10:
#             continue
#         elif num == 5:
#             sums -= num #sums = sums - num
#         else:
#             sums += num
#     print(sums)

# addition(10, 20, 30, 10, 15)  # 65
# addition(10, 20, 30, 10, 15, 5, 100)  # 160
# # >---------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# def show_skills(name, *skill):
# if len(skill) == 0:print(f"Hello {name} You Have No Skills To Show")
#     if len(skill) > 1:
#         print(f"Hello {name} Your Skills Is : ")
#         for skills in skill:
#             print(f"- {skills}")
#     else:
#         print(f"Hello {name} You Have No Skills To Show")

# show_skills("Osama")
# # >---------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# def say_hello(name="Unknown",age="Unknown",country="Unknown"):
#   return f"Hello {name} Your Age Is {age} And You Live In {country}"
# print(say_hello("Osama", 38, "Egypt"))
# ? -------------------------------------------------------------------------------------------- EX 064-060
# # >---------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# def get_score(**skills):
#     for sk, val in skills.items():
#         print(f"{sk} => {val}")

# get_score(Math=90, Science=80, Language=70, Langu=90)
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# def get_people_scores(*name, **scores):
#     for names in name:

#         if len(names) > 0 and len(scores) > 0:

#             print(f"Hello {names} This Is Your Score Table : ")

#         if len(scores) == 0:

#             print(f"Hello {names} You Have No Scores To Show")

#     for get_key, get_value in scores.items():

#         print(f"{ get_key} => {get_value}")

# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")
# # >---------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# scores_list = {
#     "Math": 90,
#     "Science": 80,
#     "Language": 70,
# }

# def get_the_scores(*name, **lists):

#     for nam in name:

#         if len(lists) > 0:

#             print(f"Hello {nam} This Is Your Score Table :")

#         else:
#             print(f"Hello {nam} You Have No Scores To Show")

#     for sco, scc in lists.items():
#         print(f"{sco} => {scc}")

# get_the_scores("OMAR",**scores_list)
# ? -------------------------------------------------------------------------------------------- EX 068-065
# # >---------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# import os
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(f"Elzero Web School => {num}")
# files_name = fr"c:\Users\omarb\OneDrive\Desktop\Python2\assign.py"

# print(files_name[-9:])

# file_num=1
# num=range(1,51)
# for alls in num:
#     if alls ==25:
#         my_files = open(fr"c:\Users\omarb\OneDrive\Desktop\Python2\special-text.txt","w")
#         my_files.close()
#     else:
#         my_files2 =open(fr"c:\Users\omarb\OneDrive\Desktop\Python2\txt{alls}.txt","w")
#         my_files2.write(f"ElZero Web School => {alls}\n")
#         my_files2.close()
#         file_num +=1
# print(file_num)
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# my_files2 =open(fr"c:\Users\omarb\OneDrive\Desktop\Python2\txt1.txt","a")
# my_files2.write(f"Appended => Elzero Web School\n"*50)
# my_files2.close()
# # >---------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# my_files2 = open(fr"c:\Users\omarb\OneDrive\Desktop\Python2\txt1.txt", "r")
# my_list = my_files2.readlines()
# lines_num = len(my_list)
# words_num = 0
# chars_num = 0
# char_1_num = 0
# for x in my_list:
#     o = x.split()
#     words_num += len(x)
#     for i in x:
#         y = i.strip()
#         chars_num += len(y)
#         char_1_num += i.count("l")
# print(f"Number Of Lines Is => {lines_num}")
# print(f"Number Of Words Is => {words_num}")
# print(f"Number Of Chars Is => {chars_num}")
# print(f"Number Of \"l\" Char Is => {char_1_num}")
# my_files2.close()
# # >---------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# import os
# for rev in range(41,51):
#     os.remove((fr"c:\Users\omarb\OneDrive\Desktop\Python2\txt{rev}.txt"))
# ? -------------------------------------------------------------------------------------------- EX 071-069
# # >---------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# values = (0, 1, 2)

# if any(values):
# any = اي عنصر من الذي بداخل المتغير
# will be True if any Element Is Ture ==> int,True,str,[element]

#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

# وهنا بسبب استخدام ال or واول قيمه صحيحه فسوف يطبع لنا Good
# True if all Element is Ture in Range OR

#   print("Good")

# else:

#   print("Bad")
# all(my_list[:4]) => True
# output => good
# # >---------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820

# for x in range(820):
#   if sum(list(range(x+1)))==820:
#     print(x)#
# >----------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# n = 21
# n = round(22)

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#     print("Good")

# for x in range(1,100):
#     if round(sum(list(range(x)))/x) ==10:
#         print(x)
# >-----------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# def my_all(*allos):
#     for x in allos:
#         if all(x) == all(allos):
#             return True
#         else:
#             return False

# print(my_all([1, 2, 3])) # True
# print(my_all([1, 2, 3, []])) # False

# def my_any(*allos):
#     for x in allos:
#         if any(x) == any(allos):
#             return True
#         else:
#             return False

# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False

# def my_min(*allos):
#     for x in allos:
#         if min(x) == min(x):
#             return f"{min(x)}"
# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100

# def my_max(*allos):
#     for x in allos:
#         if max(x) == max(x):
#             return f"{max(x)}"

# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
# ? -------------------------------------------------------------------------------------------- EX 075-072
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# def remove_chars(names):

#   return names[1:-1]

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list =map(remove_chars,friends_map)
# cleaned_list =map(lambda names:names[1:-1],friends_map)

# for i in cleaned_list:
#   print(i)

# remove_chars(friends_map)
# >-----------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# def get_names(filters):
#     return filters.endswith("m")

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# names = filter(get_names, friends_filter)
# names = filter(lambda filters:filters.endswith("m"),friends_filter)
# for x in names:
#     print(x)
# >-----------------------------------------
# ^^ Assign 3
# >-----------------------------------------
# from functools import reduce
# def multiply(num1, num2):

#     return num1*num2

# nums = [2, 4, 6, 2]
# result = reduce(multiply, nums)
# result = reduce(lambda num1,num2:num1*num2,nums)
# print(result)

# print(reduce(multiply, nums))
# >-----------------------------------------
# ^^ Assign 4
# >-----------------------------------------
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# skills=reversed(skills)

# skills =enumerate(skills,50)

# skills= list(skills)

# def cleaner(name):

#     if type(name[1])==int:

#      pass

#     else:

#         return name
# cleaned =filter(cleaner,skills)
# for i,s in cleaned:

#     print(f"{i} - {s}")

# cleaner(skills)
# ?------------------------
# skills= list(skills)

# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# skills=reversed(skills)

# skills =enumerate(skills,50)

# skills= list(skills)

# for x, s in skills:
#     if type(s)==int:
#         continue
#     else:
#         print(f"{x} - {s}")
# ? -------------------------------------------------------------------------------------------- EX 078-076
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# import random
# print(f"Random Number Between 10 And 50 => {random.randint(10,50)} ")
# >-----------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# rand = random.randint(2, 10)
# if rand== 3 or rand ==5 or rand ==7 or rand ==9:
#    pass
# else:print(f"Random Even Number Between 2 And 10 => {rand}")
# >-----
# print(f"Random Number Between Between 2 And 10 => {random.randrange(2,10,2)} ")
# >--------------------------------
# rand = random.randint(1, 9)
# if rand == 2 or rand == 4 or rand == 6 or rand == 8:
#     pass
# else:print(f"Random Even Number Between 1 And 9 => {rand}")
# >-------
# print(f"Random Even Number Between 2 And 10 => {random.randrange(1,9,2)}")
# >--------------------------------
# print(dir(random))
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# import sys,os
# sys.path.append(os.path.dirname(__file__))

# import my_mod
# print(dir(my_mod))
# my_mod.say_hello("Omar")
# my_mod.say_welcome("Omar")
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# from my_mod import say_welcome
# say_welcome("Omar")
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# from my_mod import say_welcome as new_welcome
# new_welcome("Omar")
# ? -------------------------------------------------------------------------------------------- EX 080-079
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# import datetime

# myDate = datetime.datetime(2021, 6, 25)
# myDate2 = datetime.datetime(2022, 8, 30)
# print(
#     f"Days From 2021-06-25 To 2021-08-10 Is => {(myDate2-myDate).days} Days.")
# >-----------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# dateNow = datetime.datetime(2022, 8, 30)

# print(dateNow.strftime("%Y-%m-%d"))  # 2022-08-30
# print(dateNow.strftime("%b %d, %Y"))  # "Aug 30, 2022"
# print(dateNow.strftime("%d - %b - %Y"))  # "30 - Aug - 2022"
# print(dateNow.strftime("%d / %b / %y"))  # "30 / Aug / 22"
# print(dateNow.strftime("%d / %B / %Y"))  # "30 / August / 2022"
# print(dateNow.strftime("%a, %d  %B  %Y"))  # "Tue, 30 August 2022"
# ? -------------------------------------------------------------------------------------------- EX 085-081
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# def reverse_string(my_string):
#     yield my_string[5]
#     yield my_string[4]
#     yield my_string[3]
#     yield my_string[2]
#     yield my_string[1]
#     yield my_string[0]

# for c in reverse_string("Elzero"):
#     print(c)
# >----------
# def reverse_string(my_string):
#     for x in my_string[-1::-1]:
#         yield x

# for c in reverse_string("Elzero"):
#     print(c)
# my_Gen = reverse_string("Osama")
# print(list(my_Gen))
# >----------
# def reverse_string(my_string):
#     for n in my_string:
#         yield n

# for c in iter(reverse_string("Elzero")):
#     print(c)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# def Deco(func):
#     def nestFun(*anyl):

#         print("Sugar Added From Decorators")

#         func(*anyl)

#         print("#" * 30)

#     return nestFun

# @Deco
# def make_tea():
#     print("Tea Created")

# @Deco
# def make_coffe():
#     print("Coffe Created")

# make_tea()
# make_coffe()
# ? -------------------------------------------------------------------------------------------- EX 089-086
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list,my_tuple):
#     my_data.extend(data)
# final_string=("".join(my_data)).capitalize()
# print(final_string)
# >-----------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     my_data.append(item1)
#     if len(my_data) == len("Elzero"):
#         final_string=("".join(my_data)).capitalize()
# print(final_string)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# from PIL import Image
# my_Image = Image.open("F:\Programing\Pyhton\elzero-pillow.png")
# my_Box = (400, 0, 800, 400)
# myNewImage = my_Image.crop(my_Box)
# my_Image.show()
# myConverted = myNewImage.convert("L")
# myConverted.save("f:\Programing\Pyhton\elzero1.png")
# myConverted.show()
# >--------------------------------
# my_Box2 = (0, 400, 1200, 800)
# myNewImage2 = my_Image.crop(my_Box2)
# myConverted2 = myNewImage2.convert("L")
# myrotate = myConverted2.rotate(180)
# myrotate.show()
# myrotate.save("f:\Programing\Pyhton\elzero2.png")
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# name="Osama"

# def any_type(name):
#      """
#      parameter(someone) => Person Name
#      Function TO Say Hello Yo AnyOne
#      """
#      print("Hello",name)

# print(any_type.__doc__)
# any_type(name)
# >-------
# def say_hello_to(name):
#      """

#      parameter(someone) => Person Name

#      Function TO Say Hello Yo AnyOne

#      """
#      return f"Hello {name}"
# print(say_hello_to("Osama"))
# print(say_hello_to.__doc__)
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# import os
# print(os.path.abspath(__file__))

# '''This For List Name Pepole'''
# my_friends = ["Ahmed","Osama","Sayed"]
# """MAke Function To Type names for List"""
# def say_hello(some_peoples) -> list:
#     '''Function To Type List Names'''
#     for some_one in some_peoples:
#         print(f"Hello {some_one}")
# say_hello(my_friends) #10.00/10 
# ? -------------------------------------------------------------------------------------------- EX 094-090
# >-----------------------------------------
# ^^ Assign 1
# >-----------------------------------------
# NUM = input("Add Your Number ").strip()
# if len(NUM) > 1:
#     raise IndexError("Only One Character Allowed")

# if NUM == "0":
#     raise ValueError("Number Must Be Larger Than 0")

# if NUM.isupper() or NUM.islower():
#     raise Exception("Only Numbers Allowed")

# else:
#     print(f"The Number Is {NUM}")
# >--------
# NUM = input("Add Your Number ").strip()
# if len(NUM) >1:
#     raise IndexError("Only One Character Allowed")
# elif NUM.isalpha():
#     raise Exception("Only Numbers Allowed")
# elif int(NUM) == 0:
#     raise ValueError("Number Must Be Larger Than 0")
# elif NUM.isdigit():
#     print("######################")
#     print(f"The Number Is {NUM}")
#     print("######################")
# >-----------------------------------------
# ^^ Assign 2
# >-----------------------------------------
# LETTER = input("Add Letter From A to Z : ")
# try:
#     if len(LETTER) != 1:
#         raise NameError
#     if not LETTER.isupper():
#         raise IndexError
# except NameError:
#     print("You Must Write One Character Only")
# except IndexError:
#     print("The Letter Not In A - Z")
# else:
#     print(f"You Typed {LETTER}")
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# def calculate(num1, num2) -> int:
#   return num1 + num2

# print(calculate(20, 30))
