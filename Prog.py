# This Is Comment

# ? اسم الاكستينشن (Better Comments)

# ! Comment
# ? Comment
# > Comment
# todo Comment
# _ Comment
# @@ Comment
# ^^ Comment
# C% Comment
# T^ Comment
# P# Comment
# V_ Comment
# J$ Comment
# B~ Comment

# ? Stat 2\8\2022 ElZero

# print("Back To Python")
# print("Use Python For AnyThing")
# ? -------------------------------------- 005 + 006 ------------------------------------------------------
# @@ type(البيانات الذي تريد معرفه نوعها) تستخدم لمعرفه نوع البيانات

# print(type("OMAr"))  # => String جمله او كلمه معينه مكتوبه تسمي
# print(type(1545))  # => Integer الرقم يسمي
# print(type(1.2))  # => float الرقم العشري يسمي
# print(type({1}))  # => set نوع البينات هنا
# print(type([1, 2]))  # => list نوع البيانات هنا
# print(type((1, 1)))  # => tuple نوع البيانات هنا
# print(type({"ONE": 1, "TWO": 2, "three": 3}))  # => Dictionary
# # => dict تستخدم لكتابه كلمه ومعنها
# print(type(2 == 2))  # => Boolean  -- true _ false
# ? -------------------------------------- 007 ------------------------------------------------------
# -- Varibles -- #! هي عمل متغير مثل الذب في لغه الجافا سكربت
# [1] Can Start With (a-z A-Z) Or underScore _testVar = " My Value"
# TestVar = "LSA"
# [2] Cannot Start With Number Or Special Characters
# [3] Can Include (0-9) Or UnderScore - Test500_Var = " My Value"
# [4] Cannot Include Special Characters
# [5] (Name) is Not Like (name) [ Case Sensitive] يوجد فرق بين اذا كان المتغير في حرف كبير ومتغير اخر في حرف صغير بمعني اختلاف حرف يعتبر انه ليس موجود
# ---------------------

# name = " My Value"  # Single Word => Normal --  كلمه واحد
# myName = " My Value"  # Two Words => camelCase -- بدايه الكلمه التانيه بحرف كبير
# test_var = " My Value"  # Two Words => snake_case- عمل اندرسكول بين الكلمه الاوله والثانيه
# print(test_var)
# ? -------------------------------------- 008 ------------------------------------------------------
# ---------------
# -- Variables --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution
# --------------------------------------------------------
#!                    كلمات محجوزه في اللغه
# تستخدم هذه لمعرفه الكلمات المحجوزه ف اللغه الذي لا يمكن استخدمها
# ?      help("keywords")
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not
# --------------------------------------------------------
# Reserved Words
# help("keywords")

# a, b, c = 5, 7, 10  # يمكننا عمل اكثر من متغير في نفس المكان عكس بعض لغات البرمجه

# print(a+c)
# ? -------------------------------------- 009 ------------------------------------------------------
# ----------------------------
# Escape Sequences Characters
#! \b => Back Space تعمل حذف لاخر حرف
#! \newline => Escape New Line + \ تستخدم لكتابه الكلام في سطر واحد اذا كانو منفصلين
#! \\ => Escape Back Slash لطباعه ال back slash نستخدم 2 منها
#! \' => Escape Single Quotes لطباعه ال Single Slash
#! \" => Escape Double Quotes لطباعه ال Double Slash
#! \n => Line Feed لعمل سطر جديد
#! \r => Carriage Return يحذف عدد الحروف او الارقام الذي يعد استخدمها
#! \t => Horizontal Tab لعمل tab بين الكلام
#! \xhh => Character Hex Value تستخدم لكتابه الحروف بشكل ال Hex
# ----------------------------
# print("Welcome\bPython")  # Remove e

# print("Hello\
#  im New\
#  In Python")

# print("Test Back Slash \\")

# print('Escape Single Quotes \'Single\'')
# print('Escape Double Quotes \"Double\"')

# print("Escape Single Quotes \'Single\' ")
# print("Escape Double Quotes \"Double\" ")

# print("Can We Make\nNew Line")

# print("Can We Make\rPyt")

# print("Make\ttab")

# print("\x45\x4C \x44\x45\x45\x50")
# ? -------------------------------------- 010 ------------------------------------------------------
# -------------------
#! -- Concatenation -- دمج الاسترينج مع بعض بستخدام ال +
# -------------------
# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang)
# full = msg + " " + lang
# print(full)

# a = "First \
# Second \
# Third"

# b = "A \
# B \
# C"

# print(a + "\n" + b)
# ? -------------------------------------------------------------------------------------------- EX 001-010
# Name = "ELDEEP"
# Age = 22
# Country = "ELMARG"
# outt = "Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."
# print(Name)
# print(outt)
# print(Age)
# print(Country)

# print(type(Name))
# print(type(Country))
# print(type(outt))
# ? -------------------------------------- 011 ------------------------------------------------------
# -------------
#! -- Strings -- انواع كتابه ال
# -------------
# myStringOne = 'This is Single Quote'
# myStringTwo = "This is Double Quotes"

# print(myStringOne)
# print(myStringTwo)

# # لكتابه الكلمه بشكل معين بداخل ال دابل كوت يتم عملها بهذا الشكل
# myStringThree = 'This is Single Quote "Test"'
# # لكتابه الكلمه بشكل معين بداخل ال سنجل كوت يتم عملها بهذا الشكل
# myStringFour = "This is Double Quotes 'Test'"

# print(myStringThree)
# print(myStringFour)

# myStringFive = '''First
# Second 'Test' "Test"
# Third'''  # لكتابه اكتر من سطر نستخدم 3 سنجل كوت في الاول والاخر

# myStringSix = """First
# Second "Test" \\\ 'Test'
# Third"""  # لكتابه اكتر من سطر نستخدم 3 دابل كوت في الاول والاخر

# print(myStringFive)
# print(myStringSix)
# ? -------------------------------------- 012 ------------------------------------------------------
# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------
# Indexing ( Access Single Item )

# myString = "I Love Python"

# print(myString[0])  # Index 0 => I
# print(myString[9])  # Index 9 => t

# print(myString[-1])  # Index -1 => First Character From End
# print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

# print(myString[8:11])  # yth
# print(myString[3:5])  # ov

# print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
# print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
# print(myString[:])  # Full Data

# print(myString[0::1])  # Full Data
# print(myString[::1])  # Full Data

# print(myString[::2])
# print(myString[::3])
# ? -------------------------------------- 013 ------------------------------------------------------
# ---------------------
# -- Strings Methods --
# ---------------------
#! len(a) تستخدم لمعرفه عدد العناصر الموجود عدد الحروف او الارقام
#! strip() تستخدم لازاله المسافات من كل الجوانب
#! rstrip() تستخدم لازاله المسافات من اللمين
#! lstrip() تستخدم لازاله المسافات من الشمال

# a = "     I Love Python Py   "
# print(len(a))
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# a = "###I Love Python##"  # ? اذا تم اعطاءه كلمه او حرف او اي شي وهو موجود سوف يتم حذفه
# print(a.strip("#"))
# print(a.rstrip("#"))
# print(a.lstrip("#"))

# a = "@#@#@#I Love Python@#@#@#"
# print(a.strip("@#"))
# print(a.rstrip("@#"))
# print(a.lstrip("@#"))

# # title()

# ? يجعل اول حرف ف كل كلمه كابتل واي حرف قبله رقم يحوله كابتل ايضا
# b = "I Love 2d Graphics and 3g Technology and python"
# print(b.title())

# # capitalize()

# ? خاصية capitalize() تقوم بتحويل أول حرف Capital من ال String واذا كان ال String يحتوي على جملة فيها الكثير من الكلمات فانه يقوم بتحويل اول حرف Capital من أول كلمة فقط وباقي الكلمات كل حروفها تكون Small Letter
# b = "I Love d Graphics and 3g Technology and python"
# print(b.capitalize())

# # zfill

# c, d, e, f = "1", "11", "111", "1111"

# print(c)
# print(d)
# print(e)
# print(f)

# ! يضيف عدد اصفار معينه علي حسب كام انت وضعت بداخل الاقواس وهذا يكون الافضل
# print(c.zfill(4))
# print(d.zfill(4))
# print(e.zfill(4))
# print(f.zfill(4))

#! upper() يجعل الحروف كلها كابتل

# g = "eldeep"

# print(g.upper())

#! lower() يجعل الحروف كلها صغيره

# h = "ELDEEP"

# print(h.lower())
# ? -------------------------------------- 014 ------------------------------------------------------
# ---------------------
# -- Strings Methods --
# ---------------------
# ? split() rsplit() تستخدم لتقطيع المسطره الذي تكون بين الكلام
# a = "I Love Python and PHP and MySQL"
# print(a.split())

# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))  # عند وضع شي معين موجود بداخل الاسترنج سوف يحذفه

# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3))  # تستخدم لتقطيع 3 عناصر فقط والباقي سوف يظهر بشكل طبيعي

# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3))  # ? يعمل تقطيع من الشمال

# ? center(العدد ,"") تستخدم لاضافه حروف قبل وبعد المتغير الذي سوف تستخدمه ويتم العد من بعد عدد الحروف الذي لديك
# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @

# ? count("string",Start,End) تستخدم للبحث عن عدد وجود الحرف او الكلمه الذي سوف تستخدمها
# f = "I Love Python and PHP Because PHP PHP is Easy"
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 34))  # ? تستخدم للبحث من اول كذا الي كذا

# ? swapcase() تجعل الحرف بدل ما يكون صغير تجعله كبير والعكس
# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase())
# print(h.swapcase())

# ? startswith() تستخدم لمعرفه المتغير يبداء بشي معين الذي سوف تضعه ام لا
# i = "I Love Python JavaScript"
# print(i.startswith("I"))
# print(i.startswith("J", 14))
# print(i.startswith("P", 7, 12))  # ويمكننا وضع بدايه ونهايه

# endswith()

# j = "I Love Python JS"
# print(j.endswith("S"))
# print(j.endswith("n", 7, 13))
# print(j.endswith("e", 2, 6))
# ? -------------------------------------- 015 ------------------------------------------------------
# ---------------------
# -- Strings Methods --
# ---------------------
# ? index(SubString, Start, End) تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
# a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
#! print(a.index("P", 0, 5))  # Through Error اذا لم يجد الشي الذي تبحث عنه سوف يعمل Error

# ? find(SubString, Start, End)  تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
# b = "I Love Python"
# print(b.find("o"))  # Index Number 3
# print(b.find("P", 0, 10))  # Index Number 7
# print(b.find("P", 0, 5))  # -1 اذا لم يجد الذي تبحث عنه سوف يطبع لك

#! rjust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها اللمين
#! ljust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها الشمال
# c = "Osama"
# print(c.rjust(10))
# print(c.rjust(10, "#"))

# d = "Osama"
# print(d.ljust(10))
# print(d.ljust(10, "#"))

#! splitlines() تستخدم لكي تسترجع لك list اذا كانت العناصر ليست علي سطر واحد
# e = """First Line
# Second Line
# Third Line"""

# print(e.splitlines())

# ? expandtabs() تجعلك تتحكم في عدد ال TAB
# g = "Hello\tWorld\tI\tLove\tPython"
# print(g.expandtabs(10))

# ? istitle() تستخدم لمعرفه هل اول حرف فقط في كل جمله يبداء بحرف كبير ام لا
# a = "Hell And WELCOME Snao My Wndy"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"

# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# ? isspace() تستخدم لمعرفه هل الشي المستخدم Space ام لا مسطره
# txt = "    "
# print(txt.isspace())

# ? islower() تستخدم لمعرفه هل جميع الحروف صغيره ام لا
# five = 'i love python'
# six = 'I Love Python'
# print(five.islower())
# print(six.islower())

# ? isupper() تستخدم لمعرفه هل جميع الحروف كبيره
# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"

# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# ? isidentifier() لمعرفه هل هذا الاسم يمكن استخدمه لعمل متغير ام لا
# seven = "osama_elzero"
# eight = "OsamaElzero100"
# nine = "Osama@Elzero100"

# print(seven.isidentifier())
# print(eight.isidentifier())
# print(nine.isidentifier())

# ? isalpha() تستخدم لمعرفه هل الحروف الموجوده من (a-z,A-Z)
# x = "AaaaaBbbbbb"
# y = "AaaaaBbbbbb111"
# print(x.isalpha())
# print(y.isalpha()

# ? isalnum() تستخدم لكي تعرف هل كل الموجود ارقام وحروف
# u = "AaaaaBbbbbb"
# z = "AaaaaBbbbbb111#"
# print(u.isalnum())
# print(z.isalnum())

# ? isnumeric() (0-9) تستخدم لمعرفه هل المتغر او الشي المستخدم ارقام
# a = "\u0030"  # unicode for 0
# b = "\u00B2"  # unicode for &sup2;
# c = "omar254"
# d = "1"
# e = "15"

# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())
# ? -------------------------------------- 016 ------------------------------------------------------
# ---------------------
# -- Strings Methods --
# ---------------------
# ? replace(Old Value, New Value, Count) تستخدم لتبديل شي معين بشي اخر وعلي حسب كام مره تحتاج ان تبدله

# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))
# print(a.replace("One", "1", 1))
# print(a.replace("One", "1", 2))

# ? join(Iterable) تستخدم لادخال شي معين داخل ال string

# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList))
# print(" & ".join(myList))
# print(", ".join(myList))
# print(type(", ".join(myList)))
# ttt = "KANO"
# print("-".join(ttt)) output => K-A-N-O
# ? -------------------------------------- 017 ------------------------------------------------------
# ------------------------
# ? -- Strings Formatting -- هذا الشكل القديم لل
# ------------------------
# name = "Omar"
# age = 22
# rank = 1

# print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

# print("My Name is: %s" % "Omar")
# print("My Name is: %s" % name)
# print("My Name is: %s and My Age is: %d" % (name, age))
# print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

#! %s => Omar > String عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
#! %d => 22 > Number عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
#! %f => 1.000 > Float عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
# n = "Omar"
# lg = "JavaScript"
# m = 2
# print("My Name Is %s And Learn Programing in %d MOnth My Lang Learing Is %s" % (n, m, lg))

#! Control Floating Point Number للتحكم في عدد الاصفار الذي تاتي بعد العلامه العشريه باستخدام ال %f
# myNumber = 10
# print("My Number is: %d" % myNumber)
# print("My Number is: %f" % myNumber)
# print("My Number is: %.5f" % myNumber)  # ? My Number is: 10.00000

#! Truncate String للتحكم في عدد الحروف الذي تريد عرضها ف ال %s
# myLongString = "Hello Peoples of Elzero Web School I Love You All"
# print("Message is %s" % myLongString)
# print("Message is %.14s" % myLongString)
# ? -------------------------------------- 018 ------------------------------------------------------
# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------
# name = "Omar"
# age = 22
# rank = 20

# print("My Name is: {}".format("Omar"))
# print("My Name is: {}".format(name))
# print("My Name is: {} My Age: {}".format(name, age))
# print("My Name Is: {:s} Age = {:d} & Rank Is: {:f}".format(name, age, rank))

# ? {:s} => String عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
# ? {:d} => Number عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
# ? {:f} => Float عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
# n = "Omar"
# l = "Python"
# y = 6

# print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# ? {:.3f} Control Floating Point Number للتحكم في عدد الاصفار الذي تاتي بعد العلامه العشريه باستخدام ال
# myNumber = 10
# print("My Number is: {:d}".format(myNumber))
# print("My Number is: {:f}".format(myNumber))
# print("My Number is: {:.3f}".format(myNumber))

# ? {:.5s} Truncate String تستخدم للتحكم في عدد الحروف الذي تريد عرضها ف ال
# myLongString = "Hello Peoples of Elzero Web School I Love You All"
# print("Message is {}".format(myLongString))
# print("Message is {:.23}".format(myLongString))
# print("Message is {:.13s}".format(myLongString))

# ? {:_d} Format Money بعض العلامات تستخدم لكي تضعها بين كل 3 ارقام
# myMoney = 500162350198

# print("My Money in Bank Is: {:d}".format(myMoney))
# print("My Money in Bank Is: {:_d}".format(myMoney))
# print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

# a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
# print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
# print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

# x, y, z = 10, 20, 30
# print("Hello {} {} {}".format(x, y, z))
# print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
# print("Hello {2:f} {0:f} {1:f}".format(x, y, z)) #out Hello 30.000000 10.000000 20.000000
# out Hello 30.00 10.0000 20.00000
# print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))
# print(f"Hello {z:.2f} {x:.4f} {y:.5f}")  # out Hello 30.00 10.0000 20.00000

# discount = 30  # %
# price = 499.99
# new_price = price * (1-discount/100)

# # ~~ 3.10.3. Old school (%)

# print("SALE: Get %d%% off the new PS5 and pay $%.0f instead of $%.2f." %
#       (discount, new_price, price))

# # ~ 3.10.4. Format method (.format())

# print("SALE: Get {:d}% off the new PS5 and pay ${:.0f} instead of ${:.2f}."
#       .format(discount, new_price, price))

# # ~ 3.10.5. F-string (f’’)

# print(
#     f"SALE: Get {discount:d}% off the new PS5 and pay ${new_price:.0f} instead of ${price:.2f}.")

# # ~ 3.10.6. String formatting with loop

# month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# balance = [-10.45,  50.99,  0.99,  -5.76,  100.57, -78.22]

# print('Monthly Balance')
# for mo, bal in zip(month, balance):
#     print(f'We have ${bal:.2f} left in {mo}.')

# print('{:^10}'.format('test'))
# print('{:03d}'.format(50))
# print('{:->10}'.format('test'))
# print('{:-<10}'.format('test'))
# print('{:-<10.9}'.format('xylophone'))
# print('{:05.1f}'.format(3.141592653589793))
# print('{:$>5.1f}'.format(3.141592653589793))
# print('{:0<5.1f}'.format(3.141592653589793))
# print('{: d}'.format((23)))
# print('{: 10d}'.format((23)))

# data = {'first': 'Hodor?', 'last': 'Hodor!'}
# print('{first} {last}'.format(**data))

# person = {'first': 'Jean-Luc', 'last': 'Picard'}
# print('{p[first]} {p[last]}'.format(p=person))

# data = [4, 8, 15, 16, 23, 42]
# print('{v[3]} {v[5]}'.format(v=data))

# class Plant(object):
#     type = 'Test Jango'

# print('{p.type}'.format(p=Plant()))

# class Plant(object):
#     type = 'tree'
#     kinds = [{'name': 'oak'}, {'name': 'maple'}]

# print('{p.type}: {p.kinds[1][name]}'.format(p=Plant()))

# print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=5))

# print('{:5.2f}'.format(2.7182))
# print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))

# print('{:.3} = {:.3}'.format('Gibberish', 2.7182))
# print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))

# print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))
# ? -------------------------------------------------------------------------------------------- EX 011-018
# ---------------------------------
#! -- Example --
# ---------------------------------
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
# n = "Omar"
# a = 22
# Country = "Egypt"
# print(
#     "\"Hello \'{0:s}\', How You Doing \\ \"\"\" Your Age Is \"{1:d}\"\" + And Your Country Is : {2:s}".format(n, a, Country))

# print(
#     "\"Hello \'{n:s}\', How You Doing \\ \"\"\" Your Age Is \"{a:d}\"\" + And Your Country Is : {Country:s}".format(n="Omar", a=22, Country="Egypt"))

# print(
#     "\"Hello \'{0:s}\', How You Doing \n\ \"\"\" Your Age Is \"{1:d}\"\" + \nAnd Your Country Is : {2:s}".format(n, a, Country))
#! ------------------------------------------------------------------------------------------------------------
# name = 'Elzero'

# # Needed Output
# print(name[1])  # Second Letter Is "l"
# print(name[2])  # Third Letter Is "z"
# print(name[5])  # Last Letter Is "o"
#! ------------------------------------------------------------------------------------------------------------
# name = 'Elzero'
# Needed Output

# print(name[1:4]) # "lze"
# print(name[1]+name[2]+name[3]) # lze"
# print(name[::2]) # "Ezr"
# print(name[0]+name[2]+name[4])  # "Ezr"
# print(name[4]+name[2]+name[0])  # "rzE"
#! ------------------------------------------------------------------------------------------------------------
# name = "#@#@Elzero#@#@"

# Needed Output
# print(name.strip("#@"))# Elzero
#! ------------------------------------------------------------------------------------------------------------
# num = "9"
# num1 = "15"
# num2 = "130"
# num3 = "950"
# num4 = "1500"

# print(num.zfill(4))  # 0009
# print(num1.zfill(4))  # 0015
# print(num2.zfill(4))  # 0130
# print(num3.zfill(4))  # 0950
# print(num4.zfill(4))  # 1500
#! ------------------------------------------------------------------------------------------------------------
# name_one = "Osama"
# name_two = "Osama_Elzero"

# # Needed Output
# print(name_one.rjust(20, "#"))  # ###############Osama
# print(name_two.rjust(20, "#"))# ########Osama_Elzero
#! ------------------------------------------------------------------------------------------------------------
# name_one = "OSamA"
# name_two = "osaMA"

# Needed Output
# print(name_one.swapcase())  # osAMa
# print(name_two.swapcase())  # OSAma
#! ------------------------------------------------------------------------------------------------------------
# msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# print(msg.count("Love"))  # 2
#! ------------------------------------------------------------------------------------------------------------
# msg = "I <3 Python And Although <3 Elzero"

# Needed Output
# print(msg.replace("<3", "Love", 1))  # I Love Python And Although <3 Elzero
#! ------------------------------------------------------------------------------------------------------------
# msg = "I <3 Python And Although <3 Elzero"

# Needed Output
# print(msg.replace("<3","Love"))# I Love Python And Although Love Elzero
#! ------------------------------------------------------------------------------------------------------------
# name = "Omar"
# age = 22
# country = "Egypt"

# Needed Output Using f""
# print("My Name Is {0}, And My Age Is {1:.0f}, And My Country Is {2}".format(
#     name, age, country))# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
#! ------------------------------------------------------------------------------------------------------------
# name = "ELDEEP"
# print(name.replace("D", "").swapcase())  # eleep
# print(name.replace("D", "").lower())  # eleep

# tango = "Tango Is Very Nice Very Hot"
# print(tango.replace("Very", name, 1))  # Tango Is ELDEEP Nice Very Hot

# last_test = "Brano Is Here Learn Python And JavaScript Here"
# Brano Is HowEnd Learn Python And JavaScript HowEnd
# print(last_test.replace("Here", "HowEnd", 2))
# ? -------------------------------------- 019 ------------------------------------------------------
# -------------
# -- Numbers --
# -------------
# ? Integer هذا نوع الذي يكون رقم لسه به اي كسور
# print(type(1))
# print(type(100))
# print(type(10))
# print(type(-10))
# print(type(-110))

# ? Float هذا نوع يكون بجانبه كسور
# print(type(1.500))
# print(type(100.99))
# print(type(-10.99))
# print(type(0.99))
# print(type(-0.99))

# Complex

# myComplexNumber = 5+8j

# print(type(myComplexNumber))

# print("Real Part Is: {}".format(myComplexNumber.real))
# print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex -- يمكنك تحويل نوع float الي complex
# [2] You Can Convert From Float To Int or Complex -- يمكنك تحويا نوع int الي complex
# [3] You Cannot Convert Complex To Any Type -- لا يمكن تحويل نوع complex الي اي شي اخري

# print(100)
# print(float(100))  # ? -- تحويل الي نوع float
# print(complex(100))  # ? -- تحويا الي نوع complex

# print(10.52)
# print(int(10.50))  # ? -- تحويل الي نوع int
# print(complex(10.52))  # ? -- تحويل الي نوع complex

# print(float(10+95j)); print(int(10+9j)) # ERROR
# ? -------------------------------------- 020 ------------------------------------------------------
# --------------------------
# -- Arithmetic Operators --
# --------------------------
# ? [+] Addition الجمع
# ? [-] Subtraction الطرح
# ? [*] Multiplication الضرب
# ? [/] Division القسمه
# ? [%] Modulus باقي القسمه
# ? [**] Exponent الاوس
# ? [//] Floor Division
# --------------------------
# Addition

# print(10 + 30)  # 40
# print(-10 + 20)  # 10
# print(1 + 2.66)  # 3.66
# print(1.2 + 1.2)  # 2.4

# Subtraction

# print(60 - 30)  # 30
# print(-30 - 20)  # -50
# print(-30 - -20)  # -10
# print(5.66 - 3.44)  # 2.22

# Multiplication

# print(10 * 3)  # 30
# print(5 + 10 * 100)  # 1005
# print((5 + 10) * 100)  # 1500

# Division

# print(100 / 20)  # 5.0
# print(int(100 / 20))  # 5

# ? Modulus باقي القسمه لو الرقم المقسوم عليه هيساوي عدد صحيح يبقي تساوي صفر غير كده يبقي تقربه لاقرب رقم وسوف تظهر النتيجه
# print(8 % 2)  # 0
# print(9 % 2)  # 1
# print(20 % 5)  # 0
# print(24 % 5)  # 2

# Exponent

# print(2 ** 5)  # 32
# print(2 * 2 * 2 * 2 * 2)  # 32
# print(5 ** 4)  # 625
# print(5 * 5 * 5 * 5)  # 625

# ? Floor Division تستخدم لمعرفه اقرب رقم يقبل القسمه علي الرقم المقابل له
# print(100 // 20)  # 5
# print(119 // 20)  # 5
# print(120 // 20)  # 6
# print(140 // 20)  # 7
# print(142 // 20)  # 7
# ? -------------------------------------------------------------------------------------------- EX 019-020
# Namo = 15
# Namo1 = 15.0
# Namo2 = 15+4j
# print(Namo)
# print(Namo1)
# print(Namo2)

# complexnum = 1+2j

# print("Imaginary Part Is: {}".format(complexnum.imag))  # Imaginary Part
# print("Real Part Is: {}".format(complexnum.real))  # Real Part

# num = 10
# num1 = "10"
# x = num1.replace("10", "10.0000000000")

# print("{:.10f}".format(num))
# print("{:.10f}".format(float(num)))
# print(x+"00000000000")


# num = 159.650

# print(int(num))  # 159
# print(type(int(num)))  # <class 'int'>


# print(100 - 115) -15
# print(50*30) 1500
# print(21%4) 1
# print(110//11) 10
# print(int(97/20)) 4
# ? -------------------------------------- 021 ------------------------------------------------------
# -----------------------------
# todo -- Lists  = []  -- هذا ليس نوع Array
# -----------
#! [1] List Items Are Enclosed in Square Brackets   هذا النوع متتالي
#! [2] List Are Ordered, To Use Index To Access Item  تستخدم بعدد الانديكس يبدا من الصفر
#! [3] List Are Mutable => Add, Delete, Edit   يمكننا التعديل فيها او الحذف منها
#! [4] List Items Is Not Unique   يتم كتابه العناصر وبعدها , كومه
#! [5] List Can Have Different Data Types  يمكن وضع اكثر من نوع في نفس ال list
# -----------------------------
# myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

# print(myAwesomeList)  # Whole List
# print(myAwesomeList[1])  # "Two"
# print(myAwesomeList[-1])  # True
# print(myAwesomeList[-3])  # 1

# print(myAwesomeList[1:4])  # ['Two', 'One', 1]
# print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
# print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

# print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
# print(myAwesomeList[::2])  # ['One', 'One', 100.5]

# print(myAwesomeList)
# @@ myAwesomeList[1] = 2 #تعديل علي الانديكس واحد
# @@ myAwesomeList[-1] = False #تعديل علي الانديكس سالب واحد
# @@ myAwesomeList[0:3] = ["A"]# تعديل من اول الانديكس صفر الي 2
# @@ myAwesomeList[0:3] = [1, 2, 3, 4, 5, 6]
# print(myAwesomeList)
# ? -------------------------------------- 022 ------------------------------------------------------
# -------------------
# -- Lists Methods --
# -------------------

# todo append() تستخدم لاضافه عنصر جديد الي ال list ولكن يتم اضافته ف الاخر

# myFriends = ["Osama", "Ahmed", "Sayed"]
# myOldFriends = ["Haytham", "Samah", "Ali"]

# myFriends.append("Alaa")
# myFriends.append(100)
# myFriends.append(150.200)
# myFriends.append(True)
# myFriends.append(myOldFriends)

# print(myFriends)
# print(myFriends[2])
# print(myFriends[6])
# print(myFriends[7])
# print(myFriends[7][2])

# todo extend() تستخدم لادخال كذا list مع بعض بشكل طبيعي

# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["One", "Two"]

# a.extend(b)
# a.extend(c)

# print(a)

# todo remove() تستخدم لحذف عنصر معين بداخل ال list ولكن اذا كان العنصر متكرر سوف تحذف اول عنصر فقط

# x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
# x.remove("Osama")
# print(x)

# todo sort() تستخدم لترتيب الارقام والحروف بترتيب الابجدي والحروف من الصغير للكبير وترتب نوع واحد من البيانات لبس كذا نوع
# ? sort(reverse=True) تستخدم لعكس الترتيب
# y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "B"]
# y.sort(reverse=True)
# print(y)
# todo reverse() تستخدم لعكس مكان العناصر بدل ما هو في الشمال يروح يمين وهكذا
# z = [10, 1, 9, 80, 100, "Osama", 100]
# z.reverse()
# print(z)
# ? -------------------------------------- 023 ------------------------------------------------------
# -------------------
# -- Lists Methods --
# -------------------
# todo clear() تستخدم لحذف جميع عناصر ال list
# a = [1, 2, 3, 4]
# a.clear()
# print(a)
# todo copy() تستخدم لعمل نسخ من list الي list اخري
# b = [1, 2, 3, 4]
# c = b.copy()
# print(b)  # Main List
# print(c)  # Copied List
# b.append(5)  #? عند اضافه عنصر اخر لا يظهر في ال copy
# print(b)  # Main List
# print(c)  # Copied List
# todo count() تستخدم لعد عنصر معين موجود كام مره
# d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
# print(d.count(1))
# todo index() تستخدم للبحث عن رقم الانديكس بتاع العنصر الذب سوف تعطيه له يبحث في اول انديكس
# e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
# print(e.index("Ahmed"))
# todo  insert() تستخدم لوضع عنصر معين قبل الانديكس الذي سوف تضعه
# f = [1, 2, 3, 4, 5, "A", "B"]
# f.insert(0, "Test")
# f.insert(-1, "Test")
# print(f)
# todo pop() تستخدم ايضا لحذف اخر عنصر اذا لم تعطيها index
# todo pop() تستخدم لوضع الانديكس ويرجع لك بقيمه هذا الانديكس ويحذفه من ال list
# g = [1, "Omar", 3, 4, 5, "A", "B"]
# print(g.pop(4))
# print(len(g)*g.pop(4))
# ? -------------------------------------------------------------------------------------------- EX 023-021
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[0])  # "Osama" => Method One
# print(friends.pop(0))  # "Osama" => Method Two
# print(friends[-1])  # "Mahmoud" => Method One
# print(friends.pop(-1))  # "Mahmoud" => Method Two
# ! -------------------------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[::2])  # "Osama", "Sayed", "Mahmoud"
# print(friends[1:4:2])  # "Ahmed", "Ali"
# ! -------------------------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud", "Danjo", "Mango"]

# print("{0}".format(friends[1:4]))  # ['Ahmed', 'Sayed', 'Ali']
# print(friends.pop(1)+" "+friends.pop(1)+" " +
#       friends.pop(1))  # "Ahmed", "Sayed", "Ali",
# print(friends[1:4])  # "Ahmed", "Sayed", "Ali",
# print(friends[1:4:1])  # "Ahmed", "Sayed", "Ali",
# print(friends[-4:-2])# "Ali", "Mahmoud"
# print("{0}".format(friends[3:5]))# "Ali", "Mahmoud"
# print(friends.pop(3)+" "+friends[-3])# "Ali", "Mahmoud"
# print(friends.pop(-4) + " " + friends.pop(-3))  # "Ali", "Mahmoud"
# ! -------------------------------------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# friends[3] = "Omar"
# friends[4] = "Omar"
# print(friends)
# ["Osama", "Ahmed", "Sayed", "Omar", "Omar"]
# ! -------------------------------------------------------
# friends = ["Osama", "Ahmed", "Sayed"]
# friends.insert(0, "Nasser")
# print(friends)  # ["Nasser", "Osama", "Ahmed", "Sayed"]
# friends.append("Salem")
# print(friends)  # ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# ! -------------------------------------------------------
# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# friends.remove("Nasser")
# friends.remove("Osama")
# print(friends)  # ["Ahmed", "Sayed", "Salem"]
# friends.remove("Salem")
# print(friends)# ["Ahmed", "Sayed"]
# ! -------------------------------------------------------
# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends)  # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# ! -------------------------------------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# friends.sort(reverse=False)
# friends.sort()
# print(friends)  # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# friends.sort(reverse=True)
# print(friends)  # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
# ! -------------------------------------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# print(len(friends))  # 6
# ! -------------------------------------------------------
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# print(technologies[-1][0])  # Django
# print(technologies[-1][-1])  # Web
# print(technologies[-1][2::])  # Web
# ? -------------------------------------- 024 ------------------------------------------------------
# -----------------------------
# todo -- Tuple = () --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses = ()
# ? [2] You Can Remove The Parentheses If You Want يمكن ازاله الكوس بشكل عادي بدون اي مشاكل
# ~ [3] Tuple Are Ordered, To Use Index To Access Item تكون عناصر مرتبه ونستخدم الانديكس لنصل الي العنصر
# ? [4] Tuple Are Immutable => You Cant Add or Delete لايمكن التعديل بها والحذف منها عكس ال list
# [5] Tuple Items Is Not Unique
# ? [6] Tuple Can Have Different Data Types يمكن وضع اي نوع بيانات وتكررها بشكل عادي
# _ [7] Operators Used in Strings and Lists Available In Tuples -- ال operators الذب تم استخدمها في الاسترينج و ال list تستخدم هنا بشكل عادي
# -----------------------------

# ? Tuple Syntax & Type Test نوع كتابه شكل ال Tuple

# myAwesomeTuple1 = ("Osama", "Ahmed")
# myAwesomeTuple2 = "Osama", "Ahmed"

# print(myAwesomeTuple1)
# print(myAwesomeTuple2)

# print(type(myAwesomeTuple1))
# print(type(myAwesomeTuple2))

# ? Tuple Indexing نستخدم الانديكس بشكل عادي لنصل للعنصر

# myAwesomeTupleThree = (1, 2, 3, 4, 5)
# print(myAwesomeTupleThree[0])
# print(myAwesomeTupleThree[-1])
# print(myAwesomeTupleThree[-3])

# Tuple Assign Values

# myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data

# myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
# print(myAwesomeTupleFive[1])
# print(myAwesomeTupleFive[-1])

# ? -------------------------------------- 025 ------------------------------------------------------

# -----------
# -- Tuple --
# print(f"{friends}".replace("Osama", "Elzero")) لتغير عنصر او التلاعب ب اي عنصر من عناصر ال tuple
# -----------

# Tuple With One Element

# myTuple1 = ("Osama",)  # ? لجعل نوع المتغير tuple نضع , اذا كان عنصر واحد
# myTuple2 = "Osama",

# print(myTuple1)
# print(myTuple2)

# print(type(myTuple1))
# print(type(myTuple2))

# print(len(myTuple1))
# print(len(myTuple2))

# ? Tuple Concatenation طريقه دمج البيانات بهذا الشكل

# a = (1, 2, 3, 4)
# b = (5, 6)

# c = a + b
# d = a + ("A", "B", True) + b

# print(c)
# print(d)

# todo Tuple, List, String Repeat (*) اتكرار نوع البانات نستخدم علامه الضرب

# myString = "Osama"
# myList = [1, 2]
# myTuple = ("A", "B")

# print(myString * 6)
# print(myList * 6)
# print(myTuple * 6)

# Methods => count()

# a = (1, 3, 7, 8, 2, 6, 5, 8)
# print(a.count(8))

# index()

# b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
# print("The Position of Index Is: {:d}".format(b.index(7)))
# print("The Position of Index Is: {:.8f}".format(b[5]))
# print(f"Testing SOme Programing: {b[1]}")
# print(f"The Position of Index Is: {b.index(6)}")

# ? Tuple Destruct _, تستخدم لتجاهل عنصر علي حسب مكان وقعه

# a = ("A", "B", 4, "C")

# x, y, _, z = a

# print(x)
# print(y)
# print(z)

# ? -------------------------------------------------------------------------------------------- EX 025-024
# ex = "Osama",

# print(ex)  # "Osama"
# print(type(ex))  # <class 'tuple'>

# friends = ("Osama", "Ahmed", "Sayed")

# print(f"{friends}".replace("Osama", "Elzero"))  # ("Elzero", "Ahmed", "Sayed")
# print(type(friends))  # <class 'tuple'>
# print(len(friends))  # 3 Elements

# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# nums_and_letters_one = nums + letters

# print(nums_and_letters_one)  # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# print(len(nums_and_letters_one))  # 6 Elements

# my_tuple = (1, 2, 3, 4)
# a, b, c = my_tuple[0], my_tuple[1], my_tuple[3]
# print(f"{a}\n{b}\n{c}")
# print("{0:}\n{1:}\n{2:}".format(a, b, c))
# print(f"{my_tuple[0]}\n{my_tuple[1]}\n{my_tuple[3]}")
# print(a)# 1
# print(b)# 2
# print(c)# 4
# ? -------------------------------------- 026 ------------------------------------------------------
# -----------------------------
# J$ -- Set => {} --
# ---------
# [1] Set Items Are Enclosed in Curly Braces => {}
# ^^ [2] Set Items Are Not Ordered And Not Indexed العناصر تكون لبست مرتبه
# ^^ [3] Set Indexing and Slicing Cant Be Done لا يستخدم الانديكس
# ^^ [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not يتم وضع نوع بيانات معينه ماعدا
# ^^ [5] Set Items Is Unique العناصر لا تكرر بداخلها
# -----------------------------
# Not Ordered And Not Indexed

# mySetOne = {"Osama", "Ahmed", 100}
# print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
# mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

# print(mySetThree)

# Items Is Unique

# mySetFour = {1, 2, "Osama", "One", "Osama", 1}
# print(mySetFour)
# ? -------------------------------------- 027 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# clear() لحذف العناصر

# a = {1, 2, 3}
# a.clear()
# print(a)

# union() تستخدم لاتحاد او جمع بين اكثر من set

# b = {"One", "Two", "Three"}
# c = {"1", "2", "3"}
# x = {"Zero", "Cool"}

# print(b | c | x)
# print(b.union(c, x))

# add() تستخدم لاضافه عنصر بداخل ال set
# V_ عند اضافه اكثر من عنصر نكرر الكود ونغير العنصر

# d = {1, 2, 3, 4}
# d.add(5)
# d.add(6)
# print(d)

# copy()
# e = {1, 2, 3, 4}
# f = e.copy()
# print(e)
# print(f)
# e.add(6)
# print(e)
# print(f)

# remove()  تستخدم لحذف شي معين وحين عدم وجود العنصر الذي تريد حذفه سوف يطبع ERROR
# g = {1, 2, 3, 4}
# g.remove(1)
# g.remove(7) عند حذف ليس موجود سوف يطبع لك ERRoR
# print(g)

# discard() تستخدم لحذف شي معين وحين عدم وجود العنصر الذي تريد حذفه لم يطبع ERROR

# h = {1, 2, 3, 4}
# h.discard(1)
# h.discard(7)
# print(h)

# pop() عند استخدام يطبع لك عنصر عشوائي

# i = {"A", True, 1, 2, 3, 4, 5}
# print(i.pop())

# B~ update() يعمل تحديث لل set من متغير ثاني
# j = {1, 2, 3}
# k = {1, "A", "B", 2}
# j.update(['Html', "Css"])
# j.update(k)

# print(j)
# ? -------------------------------------- 028 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# B~ difference() تستخدم لمعرفه الاختلاف بين اي 2 set
# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}
# print(a)
# print
# print(a.difference(b))  # => a - b
# print(a)

# B~ difference_update() تستخدم لمعرفه الاختلاف بين اي 2 set
# c = {1, 2, 3, 4}
# d = {1, 2, "Osama", "Ahmed"}
# print(c)
# c.difference_update(d)  # c - d
# print(c)

# J$ intersection() تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني
# e = {1, 2, 3, 4, "X"}
# f = {"Osama", "X", 2}
# print(e)
# print(e.intersection(f))  # => e & f
# print(e)

# B~ intersection_update()  تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني وتعمل تحديث للبيانات ويتم وضعهم في المتغير الاصلي
# g = {1, 2, 3, 4, "X", "Osama"}
# h = {"Osama", "X", 2}
# print(g)
# g.intersection_update(h)  # g & h
# print(g)

# B~ symmetric_difference() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود هنا ولبس موجود هنا
# i = {1, 2, 3, 4, 5, "X"}
# j = {"Osama", "Zero", 1, 2, 4, "X"}
# print(i)
# print(i.symmetric_difference(j))  # i ^ j
# print(i)

# B~ symmetric_difference_update() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود هنا ولبس موجود هنا وتعمل تحديث للمتغير الاصلي
# k = {1, 2, 3, 4, 5, "X"}
# l = {"Osama", "Zero", 1, 2, 4, "X"}
# print(k)
# k.symmetric_difference_update(l)  # k ^ l
# print(k)
# ? -------------------------------------- 029 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# B~issuperset() تستخدم لمعرف هل عناصر ال set نفس عناصر ال set الثانيه ام لا واذاك ان بعض العناصر موجوده بداخل ال set الثانيه سوف يرجع ب True

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {1, 2, 3, 4, 5}
# print(a.issuperset(b))
# print(a.issuperset(c))

# B~ issubset() تستخدم لمعرفه هل ال set الاساسيه تساوي نفس عناصر ال set الثانيه

# d = {1, 2, 3, 4}
# e = {1, 2, 3}
# f = {1, 2, 3, 4, 5}
# print(d.issubset(e))  # False
# print(d.issubset(f))  # True

# B~ isdisjoint() تستخدم لمعرفه هل كل العناصر مختتلفه عن بعض

# g = {1, 2, 3, 4}
# h = {1, 2, 3}
# i = {10, 11, 12}
# print(g.isdisjoint(h))  # False
# print(g.isdisjoint(i))  # True

# ? -------------------------------------- 030 ------------------------------------------------------

# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces => {}
# [2] Dict Items Are Contains Key : Value => {"Key":"Value","Key":"Value"}
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed يستخدم جميع انواع البيانات معادا list
# [4] Dict Value Can Have Any Data Types الادخال يمكنك استخدام جميع انواع البيانات
# [5] Dict Key Need To Be Unique لا يستحب تكرار البيانات
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

# user = {
#     "name": "Osama",
#     "age": 36,
#     "country": "Egypt",
#     "skills": ["Html", "Css", "JS"],
#     "rating": 10.5
# }

# print(type(user))

# B~ get() تستخدم للمناده علي ال key

# print(user)
# print(user["skills"][2])
# print(user["skills"][:3])
# print(user.get("skills")[1])
# print(user['country'])
# print(user.get("country"))

# print(user.keys()) تستخدم لطباعه كل ال keys
# print(user.values()) تستخدم لطباعه كل ال values

# Two-Dimensional Dictionary

# languages = {
#     "One": {
#         "name": "Html",
#         "progress": "80%"
#     },
#     "Two": {
#         "name": "Css",
#         "progress": "90%"
#     },
#     "Three": {
#         "name": "Js",
#         "progress": ["50%", "90%"]
#     }
# }

# print(languages)
# print(languages['One'])
# print(languages['Three']['name'])
# print(languages['Three']['progress'][0])

# Dictionary Length

# print(len(languages))
# print(len(languages["Two"]))

# Create Dictionary From Variables

# frameworkOne = {
#     "name": "Vuejs",
#     "progress": "80%"
# }

# frameworkTwo = {
#     "name": "ReactJs",
#     "progress": "80%"
# }

# frameworkThree = {
#     "name": "Angular",
#     "progress": "80%"
# }

# allFramework = {
#     "1st": frameworkOne,
#     "2st": frameworkTwo,
#     "3th": frameworkThree
# }

# print(allFramework)

# ? -------------------------------------- 031 ------------------------------------------------------

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

# user = {
#     "name": "Osama"
# }
# print(user)
# user.clear()
# print(user)

# update()

# member = {
#     "name": "Osama"
# }
# print(member)
# member["age"] = 36
# print(member)
# member.update({"country": "Egypt"})
# print(member)

# copy()

# main = {
#     "name": "Osama"
# }
# b = main.copy()
# print(b)
# main.update({"skills": "Fighting"})
# print(main)
# print(b)
# # keys() + values()
# print(main.keys())
# print(main.values())

# ? -------------------------------------- 032 ------------------------------------------------------

# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault() تستخدم لكي يبحث عن ال keys و value الذي سوف يتم وضعهم ان وجدهم سوف يرجع بيهم وان لم يلاقيهم سوف يعمل key جديده بال valuse الجديده

# user = {
#     "name": "Osama"
# }
# print(user)
# print(user.setdefault("newNa", 'Omar'))
# print(user)

# popitem() تستخدم لمعرفه اخر عنصر في المتغير

# member = {
#     "skill": "PS4",
#     "name": "Osama",
# }
# print(member)
# member.update({"age": 36})
# print(member.popitem())

# items() تستخدم لعرض ال keys و valuses حتي لو بعد عمل عنصر جديد

# view = {
#   "name": "Osama",
#   "skill": "XBox"
# }

# allItems = view.items()
# print(view)
# view["age"] = 36
# view.update({"NOsa":50})

# print(allItems)

# @@ fromkeys(متغير ال value , متغير ال keys) يتم عمل Dictionary من خلالها ونستخدم قبلها .dict

# a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
# b = "X"
# print(dict.fromkeys(a,b))

# ? -------------------------------------------------------------------------------------------- EX 032-026
# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list = my_list[:6]
# print(unique_list)  # 1, 2, 3, 4, 5
# print(type(unique_list))  # <class 'list'>
# unique_list.remove(5)
# print(unique_list)  # 1, 2, 3, 4
# >---------------------
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# Needed Output
# print(nums.union(letters))  # {1, 2, 3, "A", "B", "C"}

# f"{nums.update(letters)}"
# print(nums)  # {1, 2, 3, "A", "B", "C"}

# nums.symmetric_difference_update(letters)
# print(nums)# {1, 2, 3, "A", "B", "C"}
# >---------------------
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set)  # {1, 2, 3}
# my_set.clear()
# print(my_set)  # set()
# my_set.update(letters)
# my_set.remove("C")
# print(my_set)# {"A", "B"}
# my_set.discard("C")
# print(my_set)
# >---------------------
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_one.issubset(set_two))

# diCover = {"prog1": "HTML",
#            "progress1": "90%",
#            "prog2": "CSS",
#            "progress2": "90%",
#            "prog3": "Python",
#            "progress3": "30%"
#            }

# print(f"{diCover['prog1']} Progress Is {diCover['progress1']}")
# print(f"{diCover['prog2']} Progress Is {diCover['progress2']}")
# print(f"{diCover['prog3']} Progress Is {diCover['progress3']}")
# diCover.update({"prog4": "AI", "progress4": "5%"})
# print(f"{diCover['prog4']} Progress Is {diCover['progress4']}")
# ? -------------------------------------- 033 ------------------------------------------------------
# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------
# name = " "
# print(name.isspace())

# print(100 > 200)
# print(100 > 100)
# print(100 > 90)

# True Values

# print(bool("Osama"))
# print(bool(100))
# print(bool(100.95))
# print(bool(True))
# print(bool([1, 2, 3, 4, 5]))

# False Values

# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool([]))
# print(bool(False))
# print(bool(()))
# print(bool({}))
# print(bool(None))
# ? -------------------------------------- 034 ------------------------------------------------------
# -----------------------
# -- Boolean Operators --
# -----------------------
# and و
# or او
# not لا تستخدم لعكس من True الي False والعكس
# -----------------------

# age = 36
# country = "Egypt"
# rank = 10

# print(age > 16 and country == "Egypt" and rank > 0)  # True
# print(age > 16 and country == "KSA" and rank > 0)  # False

# print(age > 40 or country == "KSA" or rank > 20)  # False
# print(age > 40 or country == "Egypt" or rank > 20)  # True

# print(not age > 40)  # True
# print(not age > 22)  # Not True = False
# ? -------------------------------------- 035 ------------------------------------------------------
# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------
# x = 300  # Var One
# y = 20  # Var Two

# n = 300  # Var One
# s = 20  # Var Two

# n = n+s*
# x += y*

# n = n-s*
# x -= y*

# n = n*s*
# x *= y*

# n = n / s
# x /= y

# n = n ** s
# x **= y

# n = n % s
# x %= y

# n = n // s
# x //= y

# print(n)
# print(x)
# ? -------------------------------------- 036 ------------------------------------------------------
# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------
# Equal + Not Equal
# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal تساوي
# [ != ] Not Equal لا تساوي
# [ > ] Greater Than اكبر من
# [ < ] Less Than اصغر من
# [ >= ] Greater Than Or Equal اكبر او يساوي
# [ <= ] Less Than Or Equal اصغر او يساوي
# --------------------------
# Equal + Not Equal

# print(100 == 100)
# print(100 == 200)
# print(100 == 100.00)

# print(100 != 100)
# print(100 != 200)
# print(100 != 100.00)

# Greater Than + Less Than

# print(100 > 100)
# print(100 > 200)
# print(100 > 100.00)
# print(100 > 40)

# print(100 < 100)
# print(100 < 200)
# print(100 < 100.00)
# print(100 < 40)

# Greater Than Or Equal + Less Than Or Equal

# print(100 >= 100)
# print(100 >= 200)
# print(100 >= 100.00)
# print(100 >= 40)

# print(100 <= 100)
# print(100 <= 200)
# print(100 <= 100.00)
# print(100 <= 40)
# ? -------------------------------------- 037 ------------------------------------------------------
# ---------------------
# -- Type Conversion --
# ----------------------
# str()
# a = 10
# print(type(a))
# print(type(str(a)))

# tuple()
# c = "Osama"  # String
# d = [1, 2, 3, 4, 5]  # List
# e = {"A", "B", "C"}  # Set
# f = {"A": 1, "B": 2}  # Dictionary
# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))

# list()
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = {"A", "B", "C"}  # Set
# f = {"A": 1, "B": 2}  # Dictionary
# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))

# set()
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = ["A", "B", "C"]  # List
# f = {"A": 1, "B": 2}  # Dictionary
# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))

# dict() تطبق ع ال tuple + list فقط اذا كانو بهذا المنظر
# d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
# e = [["One", 1], ["Two", 2], ["Three", 3]]  # List
# print(dict(d))
# print(dict(e))
# ? -------------------------------------------------------------------------------------------- EX 037-033
# print(bool(1))  # True
# print(bool(True))  # True
# print(bool("Omar"))  # True
# print(bool("10>5"))  # True
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool())  # False
# print(bool(None))  # False

# html = 80
# css = 60
# javascript = 70
# Needed Output
# print(html > 50 and css > 50 and javascript > 50) # True

# num_one = 10
# num_two = 20
# num = 20
# print(num > num_one or num > num_two)  # True
# print(num > num_one and num > num_two)  # False

# num_one = 10
# num_two = 20
# result = num_two + num_one
# print(result)  # 30
# print(result**3)  # 27000
# print(result**3//27)  # 1000
# print(result**3//27/5)  # 200.0
# print(type(str(result**3//27/5)))  # <class 'str'>
# ? -------------------------------------- 038 ------------------------------------------------------
# ----------------
# -- User Input --
# ----------------
# input("Type Ur Age : ")
# fName = input('What\'s Is Your First Name?')
# mName = input('What\'s Is Your Middle Name?')
# lName = input('What\'s Is Your Last Name?')
# fName = fName.strip().capitalize()
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()
# print(f"Hello {fName.strip()} {mName.strip()} {lName.strip()} Happy To See You.")
# print(f"Hello {fName} {mName:.1} {lName} Happy To See You.")
# ? -------------------------------------- 039 ------------------------------------------------------
# ---------------------------
# -- Practical Slice Email --
# ---------------------------
# theName = input('What\'s Your Name ?').strip().capitalize()
# theEmail = input('What\'s Your Email ?').strip()

# theUsername = theEmail[:theEmail.index("@")]
# theWebsite = theEmail[theEmail.index("@") + 1:]

# print(f"Hello {theName} Your Email Is {theEmail}")
# print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])
# ? -------------------------------------- 040 ------------------------------------------------------
# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------
# Input Age
# age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print('You Lived For:')
# print(f"{months} Months.")
# print(f"{weeks:,} Weeks.")
# print(f"{days:,} Days.")
# print(f"{hours:,} Hours.")
# print(f"{minutes:,} Minutes.")
# print(f"{seconds:,} Seconds.")
# ? -------------------------------------------------------------------------------------------- EX 040-038
# name = (input("Type Ur Name : "))
# print(f"Hello {name.strip().capitalize()}, Happy To See You Here.")

# name = (input("Type Ur Name : ")).strip().capitalize()
# print(f"Hello {name}, Happy To See You Here.")

# age = (int(input(" Type Ur Age : ").strip()))
# age < 16 == print(
#     f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")# If Age < 16

# age >= 16 == print(
#     f"Hello Your Age Is {age}, All Articles Is Suitable For You")# If Age Is 16+
# ------------------------------------------
# if age < 16:
#     print(f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")# If Age < 16

# elif age >= 16:
#     print("Hello Your Age Is {}, All Articles Is Suitable For You".format(age))# If Age Is 16+
# ------------------------------------------
# first_name=input(" Type Ur fName : ").strip().capitalize()
# second_name=input(" Type Ur lName : ").strip().capitalize()

# print(f"Hello {first_name} {second_name:.1s}.") # Example "Omar A."
# ------------------------------------------
# theUsername = theEmail[:theEmail.index("@")]
# email = input("Type Ur Email : ").strip().lower()
# userName = email[:email.index("@")]
# theEmail = email[email.index("@")+1:-4]
# theEmail = email[email.index("@")+1:email.index(".")]
# dominName = email[email.index(".")+1:]
# print(f"Your Name Is {userName}")
# print(f"Email Service Provider Is {theEmail}")
# print(f"Top Level Domain Is {dominName}")
# ? -------------------------------------- 041 ------------------------------------------------------
# --------------------
# --  Control Flow  --
# -- If, Elif, Else -- لو - او لو - غير ذالك
# -- Make Decisions --
# --------------------
# uName = "Shark"
# uCountry = "Egypt"
# cName = "Python Course"
# cPrice = 100

# C% if uCountry == "Egypt":  # تستخدم لعمل شرط

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# C% elif uCountry == "KSA":  # تستخدم لعمل شرط اخر غير الاول

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

# C% elif uCountry == "Kuwait":  # تستخدم لعمل شرط اخر غير الاول و الثاني

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# C% else:  # تستخدم حين عدم تحقيق اي شرط من السابقين

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
# -----------------------------------------------------------
# uName = input(" Type Ur userName : ").upper()
# uCountry = input(" Type Ur Country : ")
# cName = input("Type Ur Course Name : ")
# cPrice = 100

# if uCountry == "Egypt":  # تستخدم لعمل شرط

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# elif uCountry == "KSA":  # تستخدم لعمل شرط اخر غير الاول

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

# elif uCountry == "Kuwait":  # تستخدم لعمل شرط اخر غير الاول و الثاني

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else:  # تستخدم حين عدم تحقيق اي شرط من السابقين

#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

# ? -------------------------------------- 042 ------------------------------------------------------
# ---------------
# -- Nested If -- واحده بداخل واحده
# ---------------
# uName = "Shark"
# isStudent = "Yes"
# uCountry = "Egypt"
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Because Student")

#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")
# elif uCountry == "Kuwait" or uCountry == "Bahrain":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Because Student")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 40}")
# else:
#     print(f"Hi {uName} Because UR From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
# -----------------------------------------------------------

# uName = input("Type Ur userName : ").capitalize()
# isStudent = input("You Are Student : ").capitalize()
# uCountry = input("Type Ur Country : ")
# cName = input("Type Ur Course Name : ").upper()
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Because Student")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")
# elif uCountry == "Kuwait" or uCountry == "Bahrain":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Because Student")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 40}")
# else:
#     print(f"Hi {uName} Because UR From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

# ? -------------------------------------- 043 ------------------------------------------------------

# ----------------------------------
# -- Ternary Conditional Operator -- اختصرتها
# ----------------------------------

# country = "A"

# if country == "Egypt":
#     print(f"The Weather in {country} Is 15")
# elif country == "KSA":
#     print(f"The Weather in {country} Is 30")
# else:
#     print("Country is Not in The List")

# Short If

# movieRate = 18
# age = 18

# if age < movieRate :

#   print("Movie S Not Good 4U") # Condition If True

# else :

#   print("Movie S Good 4U And Happy Watching") # Condition If False

# print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False

# ? -------------------------------------- 044 ------------------------------------------------------
# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------
# Write A Very Beautiful Note
# print("#" * 80)
# print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
# print("#" * 80)

# Collect Age Data
# age = input("Please Write Your Age : ").strip()

# Collect Time Unit Data
# unit = input("Please Choose Time Unit: Months, Weeks, Days : ").strip().lower()

# Get Time Units
# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == 'months' or unit == 'm':
#     print("You Choosed The Unit Months")
#     print(f"You Lived For {months:,} Months.")

# elif unit == 'weeks' or unit == 'w':

#     print("You Choosed The Unit Weeks")
#     print(f"You Lived For {weeks:,} Weeks.")

# elif unit == 'days' or unit == 'd':

#     print("You Choosed The Unit Days")
#     print(f"You Lived For {days:,} Days.")
# ? -------------------------------------- 045 ------------------------------------------------------
# --------------------------
# -- Membership Operators --
# --------------------------
# in هل العنصر موجود بداخل
# not in هل العنصر ليس موجود
# --------------------------

# String

# name = "Osama"
# print("s" in name)
# print("a" in name)
# print("A" in name)

# print("#" * 50)

# List

# friends = ["Ahmed", "Sayed", "Mahmoud"]
# print("Osama" in friends)
# print("Sayed" in friends)
# print("Mahmoud" not in friends)  # هل محمود ليس موجود

# Using In and Not In With Condition

# countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
# countriesOneDiscount = 80

# countriesTwo = ["Italy", "USA"]
# countriesTwoDiscount = 50

# myCountry = "Italy"

# if myCountry in countriesOne:

#     print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

# elif myCountry in countriesTwo:

#     print(f"Hello You Have A Discount Equal => ${countriesTwoDiscount}")

# else:

#     print("You Don't Have Discount")

# @@ --------------------------------------------- تم استخدام الشكل الذي فوق بدل الي تحت اختصار

# if myCountry == "Egypt" or "KSA" or "Kuwait" or "Bahrain" or "Syria":

#     print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

# elif myCountry == "Italy" or "USA":

#     print(f"Hello You Have A Discount Equal => ${countriesTwoDiscount}")

# else:

#     print("You Don't Have Discount")
# ? -------------------------------------- 046 ------------------------------------------------------
# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# # Login
# name = input('Type Ur UserAdmin : ').strip().capitalize()

# # If Name is In Admin
# if name in admins:

#     print(f"Hello {name} Welcome In Admin Page")

#     option = input(
#         'Type You Option > Delete or Update : ').strip().capitalize()

# # Update Option
#     if option == "Update" or option == "U":
#         theNewName = input("Type Your Name Update To : ").strip().capitalize()
#         admins[admins.index(name)] = theNewName
#         print("Name Updated.")
#         print(admins)

#  # Delete Option
#     elif option == "Delete" or option == 'D':
#         print(f" Len Before: {len(admins)}")
#         admins.remove(name)
#         print("Admin Deleted")
#         print(f"Len After: {len(admins)}")
#         print(admins)

# # Wrong Option
#     else:
#         print("Wrong Option Choosed")
# else:
#     status =input("Not Admin, Add You Y, N ? ").strip().capitalize()
#     if status == "Yes" or status == "Y":
#         print("You Have Been Added")
#         admins.append(name)
#         # admins.insert(0,name)
#         print(admins)
#     else:
#         print("You Are Not Added.")

# ? -------------------------------------------------------------------------------------------- EX 046-041

# num1 = int(input("Type Your Number ID : ").strip())
# num2 = int(input("Type Your Number ID2 : ").strip())
# operation = input("Choose Any operation + or - or * or / or % : ").strip()

# if operation =="+":
#     print(f"{num1} + {num2} =", num1 + num2)
# elif operation =="-":
#     print(f"{num1} - {num2} =", num1 - num2)
# elif operation =="*":
#     print(f"{num1} * {num2} =", num1 * num2)
# elif operation =="/":
#     print(f"{num1} / {num2} =", num1 / num2)
# elif operation =="%":
#     print(f"{num1} % {num2} =", num1 % num2)
# else:
#     print("Plase Choose Any Operation")
# -------------------------------
# age = 15
# print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")
# -------------------------------
# uAge = int(input("Type You Age : "))
# if uAge >= 10 and uAge <= 100:
#     month = uAge * 12
#     print(f"Your Age In Months => \"{month:,}\" Months")
#     weeks = month * 4
#     print(f"Your Age In Months => \"{weeks:,}\" Weeks")
#     days = weeks * 365
#     print(f"Your Age In Months => \"{days:,}\" Days")
#     hours = days * 24
#     print(f"Your Age In Months => \"{hours:,}\" Hours")
#     minute = hours * 60
#     print(f"Your Age In Months => \"{minute:,}\" Minutes")
#     seconds = minute * 60
#     print(f"Your Age In Months => \"{seconds:,}\" Seconds")
# else:
#     print("You Are Very Older Go Back To You Family")
# -------------------------------
# country = input("Input Your Country : ").strip().capitalize()
# countryGest = ["Egypt", "Palestine", "Syria",
#                "Yemen", "Ksa", "Usa", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countryGest:
#     print(f"Your Country Eligible Your Discount After Is ${price-discount}")
# else:
#     print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# ? -------------------------------------- 047 ------------------------------------------------------
# -------------------
# -- Loop => While -- تستخدم لعمل تكرار علي البيانات
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

# a = 0

# while a < 15:

#     print(a)

#     a += 1  # a = a + 1

# else:
#     print("Loop is Done")  # True Become False

# while False:

#     print("Will Not Print")
# ? -------------------------------------- 048 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

# myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# a = 0
# while a < len(myF):
#     print(f"#{str(a+1).zfill(2)} {myF[a]}")
#     a += 1
# else:
#     print("Your Loop Done")

# ? -------------------------------------- 049 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
# myFavouriteWebs = []

# # Maximum Allowed Websites
# maximumWebs = 5

# while maximumWebs > 0:

#   # Input The New Website
#   web = input("Website Name Without https:// ")

#   # Add The New Website To The List
#   myFavouriteWebs.append(f"https://{web.strip().lower()}")

#   # Decrease One Number From Allowed Websites
#   maximumWebs -= 1  # maximumWebs = maximumWebs - 1

#   # Print The Add Message
#   print(f"Website Added, {maximumWebs} Places Left")

#   # Print The List
#   print(myFavouriteWebs)

# else:

#   print("Bookmark Is Full, You Cant Add More")

# # Check If List Is Not Empty
# if len(myFavouriteWebs) > 0:

#   # Sort The List
#   myFavouriteWebs.sort()

#   index = 0

#   print("Printing The List Of Websites in Your Bookmark")

#   while index < len(myFavouriteWebs):

#     print(myFavouriteWebs[index])

#     index += 1  # index = index + 1
# ? -------------------------------------- 050 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------
# tries = 4

# mainPassword = "Osama@123"

# inputPassword = input("Write Your Password: ")

# while inputPassword != mainPassword:  # True

#     tries -= 1  # tries = tries - 1

#     print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

#     inputPassword = input("Write Your Password: ")

#     if tries == 0:

#         print("All Tries Is Finished.")

#         break

#         print("Will Not Print")

# else:

#     print("Correct Password")
# ? -------------------------------------------------------------------------------------------- EX 050-047
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
# -------------------------------------
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

# print(f"Friends Printed And Ignored Names Count Is {len(frino)}")
# -------------------------------------
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# while skills:
#     print(f"{skills[0]}\n{skills[1]}\n{skills[2]}\n{skills[3]}\n{skills[4]}");break
# while skills:
#     print(f"{skills[:]}");break
# -------------------------------------
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
#             f"Friend {pplName} Added => {len(my_friends)}st Letter Become Capital")
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

# Sort The List
# my_friends.sort()

# index = 0

# while index < len(my_friends):

#     print(my_friends[index])

#     index += 1  # index = index + 1
# print(my_friends)
# ? -------------------------------------- 051 ------------------------------------------------------
# -----------------
# -- Loop => For --
# -----------------
# @@ for item in iterable_object : استخدمها سهل يعتمعد علي اسم لل Loop ثم المتغير الذي تعمل عليه Loop
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ] تاخذ جميع انواع البيانات
# ---------------------------------------------------------------
# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in myNumbers:

#     # print(number * 17)

#     if number % 2 == 0:  # Even

#         print(f"The Number {number} Is Even.")

#     else:

#         print(f"The Number {number} Is Odd.")

# else:

#     print("The Loop Is Finished")

# myName = "Osama", "OMAR"

# for letter in myName:

#     print(f" [ {letter.lower()} ] ")
# ? -------------------------------------- 052 ------------------------------------------------------
# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------
# Range

# myRange = range(1, 101, 2)

# for number in myRange:

#     print(number)

# Dictionary

# mySkills = {
#     "Html": "98%",
#     "Css": "93%",
#     "PHP": "70%",
#     "JS": "94%",
#     "Python": "49%",
#     "MySQL": "30%"
# }

# print(mySkills['JS'])
# print(mySkills.get("Python"))

# for skills in mySkills:
#     print(f"My Progress in Lang {skills} Is: {mySkills[skills]}")
#     print(f"My Progress in Lang {skills} Is: {mySkills.get(skills)}")
# ? -------------------------------------- 053 ------------------------------------------------------
# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------
# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'Js']

# for name in peoples:  # Outer Loop

#     print(f"{name} Skills Is: ")

#     for skill in skills:  # Inner Loop

#         print(f"- {skill}")

# Dictionary

# peoples = {
#     "Osama": {
#         "Html": "70%",
#         "Css": "80%",
#         "Js": "70%"
#     },
#     "Ahmed": {
#         "Html": "90%",
#         "Css": "80%",
#         "Js": "90%"
#     },
#     "Sayed": {
#         "Html": "70%",
#         "Css": "60%",
#         "Js": "90%"
#     }
# }

# print(peoples["Osama"])
# print(peoples["Ahmed"])
# print(peoples["Sayed"])

# print(peoples["Osama"]['Css'])
# print(peoples["Ahmed"]['Css'])
# print(peoples["Sayed"]['Css'])

# for name in peoples:

#     print(f"Skills and Progress For {name} Is: ")

#     for skill in peoples[name]:

#         print(f"{skill.capitalize()} => {peoples[name][skill]}")
# ? -------------------------------------- 054 ------------------------------------------------------
# > ------------------------
# -- Break, Continue, Pass --
# todo Continue تستخدم لتفادي شي معين او عنصر معين
# todo Break تستخدم للتوقف عند عنصر معين سوف توقف ال Loop
# todo Pass تستخدم لعبور او تفادي loop معين
# > ------------------------
# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Continue

# for nums in myNumbers:
#     if nums == 8:
#         continue
#     print(nums)

#  Break

# for nums in myNumbers:
#     print(nums) #J$ تفرق بين ان تطبع قبل ال break ام لا
#     if nums == 8:
#         break
# print(nums) #V_ تفرق بين ان تطبع قبل ال break ام لا

# Pass

# for number in myNumbers:
#     if number == 13:
#         pass
#     print(number)
# ? -------------------------------------- 055 ------------------------------------------------------
# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------
# mySkills = {
#   "HTML": "80%",
#   "CSS": "90%",
#   "JS": "70%",
#   "PHP": "80%"
# }
# print(mySkills.items())
# #######################
# for skill in mySkills:
#   print(f"{skill} => {mySkills[skill]}")
# #######################
# for skill_key, skill_progress in mySkills.items():
#   print(f"{skill_key} => {skill_progress}")
# #######################
# myUltimateSkills = {
#   "HTML": {
#     "Main": "80%",
#     "Pugjs": "80%"
#   },
#   "CSS": {
#     "Main": "90%",
#     "Sass": "70%"
#   }
# }
# for main_key, main_value in myUltimateSkills.items():
#   print(f"{main_key} Progress Is: ")
#   for child_key, child_value in main_value.items():
#     print(f"- {child_key} => {child_value}")
# ? -------------------------------------------------------------------------------------------- EX 055-051
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# for nums in my_nums:
#     print(nums)
#     if nums % 5 == 0:
#         # print(nums)
#         pass
# else:
#     print("Loop Is Sussfully")
# > ---------------------------
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
# > ---------------------------
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
#     print(f"Total Points Is {abc.pop(0)+abc.pop(0)+abc.pop(0)+abc.pop(0)}")
# > ---------------------------
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
# print("------------------------------")
# for stud in students:
#     abcd = []
#     print(f"-- Student Name => {stud}")
#     print("------------------------------")
#     for st in students[stud]:
#         if students[stud][st] == "A":
#             print(f"- {st} => {A} Points")
#             abcd.append(A)
#         elif students[stud][st] == "B":
#             print(f"- {st} => {B} Points")
#             abcd.append(B)
#         elif students[stud][st] == "C":
#             print(f"- {st} => {C} Points")
#             abcd.append(C)
#         elif students[stud][st] == "D":
#             print(f"- {st} => {D} Points")
#             abcd.append(D)
#     print(
#         f"Total Points For {stud} Is {abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)}")
#     print("------------------------------")
# > ---------------------------
# print("------------------------------")
# for stud, mains in students.items():
#     abcd = []
#     print(f"-- Student Name => {stud}")
#     print("------------------------------")
#     for studo, childs in mains.items():
#         if childs == "A":
#             print(f"- {studo} => {A} Points")
#             abcd.append(A)
#         elif childs == "B":
#             print(f"- {studo} => {B} Points")
#             abcd.append(B)
#         elif childs == "C":
#             print(f"- {studo} => {C} Points")
#             abcd.append(C)
#         elif childs == "D":
#             print(f"- {studo} => {D} Points")
#             abcd.append(D)
#     print(f"Total Points For {stud} Is {abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)+abcd.pop(0)}")
#     print("------------------------------")
# ? -------------------------------------- 056 ------------------------------------------------------
# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# J$ def name():
# B~ def تستخدم لعمل متغير معين ومانداته بعد كده
# B~ return تستخدم لاسترجاع البيانات الذي بداخل ال function
# ----------------------------------------
# def function_name():

#   return "Hello Python From Inside Function"

# dataFromFunction = function_name()

# print(dataFromFunction)
# ? -------------------------------------- 057 ------------------------------------------------------
# ---------------------------------------
# -- Function Parameters And Arguments --
# V_ تستخدم بشكل طبيعي وعادي جدا زي باقي الاشياء لا يوجد فرق
# ---------------------------------------
# a, b, c = "Osama", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

# def say_hello(n):

#   print(f"Hello {n}")

# say_hello(a)
# say_hello(b)
# say_hello(c)

# def addition(n1, n2):

#   print(n1 + n2)

# addition(100, 300)
# addition(-50, 100)

# def addition(n1, n2):

#   if type(n1) != int or type(n2) != int:

#     print("Only Integers Allowed")

#   else:

#     print(n1 + n2)

# addition(100, 500)

# def full_name(first, middle, last):

#   print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

# full_name("   osama   ", 'mohamed', "elsayed")
# ? -------------------------------------- 058 ------------------------------------------------------
# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# _ ترجع لك بقائمة Tuple
# * تستخدم لاسترجاع البيانات بشكل عادي print(*myList)
# -------------------------------------------------
# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print(*myList)

# def say_hello(*pepole): #@@ تستخدم عند عدم معرفه عدد العناصر الذي لديك او بيتم زياده او التعديل كل فتره

#     for name in pepole:

#         print(f"Hello {name}")

# say_hello("Osama", "Ahmed", "Sayed", "Mahmoud") #@@ ياخذ عدد غير محدود من العناصر

# def show_details(name, *skills):

#     print(f"Hello {name} Your Skills Is :")

#     for skill in skills:

#         print(skill)

# show_details("OSman", "HTML", "CSS", "JS", "Python", "MySQL")
# ? -------------------------------------- 059 ------------------------------------------------------
# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------
# def say_hello(name="Unknown", age="Unknown", country="Unknown"):

#   print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

# say_hello("Osama", 36, "Egypt")
# say_hello("Mahmoud", 28, "KSA")
# say_hello("Sameh", 38)
# say_hello("Ramy")
# say_hello()
# ? -------------------------------------------------------------------------------------------- EX 059-056
# ^^ Assign 1
# -----------------------------------
# def calculate(num1, num2, name="Free"):
#     a = num1 + num2
#     c = num1 - num2
#     b = num1 * num2
#     if a == num1+num2 and name == "Free":
#         print(a)
#     else:
#         if a == num1+num2 and name == "add" or name == 'a' or name == 'A' or name == 'AdD' or name == 'adD' or name == 'ADD':
#             print(f"{a} Cal Plass")
#         else:
#             print("This Calculate Is ERRoR")
#         if c == num1-num2 and name == 'S' or name == 'subTRACT' or name == 'subtract' or name == 's':
#             print(f"{c} Cal subtract")
#         else:
#             print("This Calculate Is ERRoR")
#         if b == num1*num2 and name == 'Multiply' or name == 'm' or name == 'multiply':
#             print(f"{b} Cal Multiply")
#         else:
#             print("This Calculate Is ERRoR")
# calculate(10, 20, "a")
# >-----------------------------------
# def calculate(num1, num2, operation="add"):
#     # operation = operation.lower()
#     if operation in ["a", "add", 'AdD', "A"]:
#         print(num1+num2)
#     elif operation in ["S", "subTRACT", "subtract", "s"]:
#         print(num1-num2)
#     elif operation in ["m", "multiply", "Multiply", "M"]:
#         print(num1*num2)
# calculate(10, 20, "M")
# >----------------------------------
# ^^ Assign 2
# -----------------------------------
# def addition(*Parameters):
#     sum = 0
#     for num in Parameters:
#         if num == 10:
#             continue
#         elif num == 5:
#             sum -= num
#         else:
#             sum += num
#     print(sum)
# addition(10, 20, 30, 10, 15, 10)
# addition(10, 20, 30, 10, 15, 5, 100)
# >----------------------------------
# ^^ Assign 3
# >----------------------------------
# def skills(name, *skill):
#     if len(skill) > 0:
#         print(f"Hello {name} Your Skills Is ")

#         for skills in skill:
#             print(f" -{skills}")
#     else:
#         print(f"Hello {name} You Have No Skills To Show")

# skills("Omar", "HTML", "CSS", "JS", "Python")
# >----------------------------------
# ^^ Assign 4
# >----------------------------------
# def say_hello(name="Unknown",age="Unknown",country="Unknown"):
#     print(f"Hello {name} Your Age Is {age} And You Live In {country}")
# say_hello("Osama", 38, "Egypt")
# say_hello("Osama", 38)
# ? -------------------------------------- 060 ------------------------------------------------------
# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# _ ترجع لك بقائمة Dict
# ----------------------------------------------------
# def show_skills(*skills): الشكل التقليدي

#   print(type(skills))

#   for skill in skills:

#     print(f"{skill}")

# show_skills("Html", "CSS", "JS")

# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%"
# }

# def show_skills(**skills):# الشكل الجديد

#   print(type(skills))

#   for skill, value in skills.items():

#     print(f"{skill} => {value}")

# show_skills(**mySkills)
# ? -------------------------------------- 061 ------------------------------------------------------
# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

# def show_skills(name, *skills,**skillsWithProgress):

#     print(f"Hello {name} \nSkills Without Progress Is: ")

#     for skill in skills:

#         print(f"- {skill}")

#     print("Skills With Progress Is: ")

#     for skill_key,skill_value in skillsWithProgress.items():

#         print(f"{skill_key} => {skill_value}")

# show_skills("Omar", "Js",Python="60%")
# > -----------------------------------------------------
# myTuple = ("Html", "CSS", "JS")

# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }

# def show_skills(name, *skills, **skillsWithProgres):

#   print(f"Hello {name} \nSkills Without Progress Is: ")

#   for skill in skills:

#     print(f"- {skill}")

#   print("Skills With Progress Is: ")

#   for skill_key, skill_value in skillsWithProgres.items():

#     print(f"- {skill_key} => {skill_value}")

# show_skills("Osama", *myTuple, **mySkills)

# ? -------------------------------------- 062 ------------------------------------------------------
# --------------------
# -- Function Scope --
#! لتحويل متغير من local الي Global نستخدم كلمه global ثم اسم المتغير
# --------------------
# x = 1  # Global Scope

# def one():

#   global x # لتحويل متغير من local الي Global نستخدم كلمه global ثم اسم المتغير

#   x = 2

#   print(f"Print Variable From Function Scope {x}")

# def two():

#   x = 10

#   print(f"Print Variable From Function Scope {x}")

# one()
# print(f"Print Variable From Global Scope {x}")
# two()
# print(f"Print Variable From Global Scope After One Function Is Called {x}")
# ? -------------------------------------- 063 ------------------------------------------------------
# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------
# Test Word [ WWWoooorrrldd ] # print(x[1:])

# x="WWWoooorrrldd"

# def cleanWord(word):

#   if len(word) == 1:

#     return word

#   print(f"Print Start Function {word}")

#   if word[0] == word[1]:

#     print(f"Print Before Condition {word}")

#     return cleanWord(word[1:])

#   print(f"Print Before Return {word}")

#   return word[0] + cleanWord(word[1:])

# Stash [ World ]

# print(cleanWord(x))
# ? -------------------------------------- 064 ------------------------------------------------------
# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------
# def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"

# hello = lambda name, age : f"Hello {name} your Age Is: {age}" #todo تستخدم لعمل function مجهولة

# print(say_hello("Ahmed", 36))
# print(hello("Ahmed", 36))

# print(say_hello.__name__)
# print(hello.__name__)

# print(type(hello))
# ? -------------------------------------------------------------------------------------------- EX 064-060
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# def get_score(**scores):

#     for score_key, score_value in scores.items():

#         print(f"{score_key} => {score_value}")

# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
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
# >--------------------
# def get_pepole_scores2(namee="", **scoress):
#     if len(scoress) > 0:

#         if bool(namee):

#             print(f"Hello {namee} This is Your Score Table: ")

#         for key, value in scoress.items():

#             print(f"- {key} => {value}")
#     else:
#         print(f"Hello {namee} You Have No Scores To Show")

# get_pepole_scores2("Osama", Math=90, Science=80, Language=70)
# get_pepole_scores2("Mahmoud", Logic=70, Problems=60)
# get_pepole_scores2(Logic=70, Problems=60)
# get_pepole_scores2("Ahmed")
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# scores_list = {
#     "Math": 90,
#     "Science": 80,
#     "Language": 70,
# }
# def get_the_scores(*name, **lists):
#     for names in name:

#         if len(lists) == 0:

#             print(f"Hello {names} You Have No Scores To Show")

#         if len(lists) > 0:

#             print(f"Hello {names} This Is Your Score Table : ")

#     for key, value in lists.items():

#         print(f"{key} => {value}")
# >-------------
# scores_list = {
#     "Math": 90,
#     "Science": 80,
#     "Language": 70,
# }
# def get_the_scores(namee="", **scoress):
#     if len(scoress) > 0:

#         if bool(namee):

#             print(f"Hello {namee} This is Your Score Table: ")

#         for key, value in scoress.items():

#             print(f"- {key} => {value}")
#     else:
#         print(f"Hello {namee} You Have No Scores To Show")
# >--------------------
# >----
# test 1
# >----
# get_the_scores("Omar",**scores_list)
# Hello Omar This Is Your Score Table :
# Math => 90
# Science => 80
# Language => 70
# >----
# test 2
# >----
# get_the_scores("Omar") # Hello Omar You Have No Scores To Show
# >----
# test 3
# >----
# get_the_scores(**scores_list)
# Math => 90
# Science => 80
# Language => 70

# _I
# ? -------------------------------------- 065 ------------------------------------------------------
# _I
# -------------------
# -- File Handling --
# -------------------
# @@ يفتح الفايل ويمكن اضافه به عناصر جديده و لو الفايل مش موجود بيعمله
# "a" Append  Open File For Appending Values, Create File If Not Exists

# @@ يفتح الملف للقراءه لو الملف مش موجود سوف يعمل ERROR
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists

# @@ يفتح الملف للكتابة في ولو الملف مش موجود سوف يتم انشاء
# "w" Write   Open File For Writing, Create File If Not Exists

# @@ يعمل لك ملف جديد لو لقي الملف هيعمل ERROR
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

# @@ المكان الذي تريد عمل به الملف بشكل تفصيل
# file = open("f:\Programing\Pyhton\Omar.txt") هذا شكل المسار الطبيعي

# os = operating system
# import os
# @@  تستخدم لمعرفه مسار الملف الذي نحن به الذي نحن فتحينه ف ال VSCODE
# Main Current Working Directory
# print(os.getcwd())

# @@ نستخدم هذا لمعرفه المسار بالتفصيل الذي نحن به
# print(os.path.abspath(__file__))
# f:\Programing\Pyhton\Prog.py

# نستخدم هذا لمعرفه المسار الملف الذي نستخدمه
# print(os.path.abspath("Prog.py"))
# f:\Programing\Pyhton\Prog.py

# V_ Directory For The Opened File لمعرفه مكان الملف الذي استخدمه حاليا
# print(os.path.dirname(os.path.abspath(__file__)))

# @@ Change Current Working Directory تغير مكان الملف الي مكان الذي نحن به بمعني اذا كان الملف الذي نستخدمه في مكان تاني سوف ينقله الي المكان الذي انت به
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

# @@ نستخدم حرف ال r قبل المسار لكي يعرف ان هذا مكان الملف
# file = open(r"f:\Programing\Pyhton\nfiles\Omar.txt")

# B~ file = open("f:\Programing\Pyhton\Omar.txt") هذا شكل المسار الطبيعي
# ? -------------------------------------- 066 ------------------------------------------------------
# --------------------------------
# -- File Handling => Read File --
# --------------------------------

# myFile = open("F:\Programing\Pyhton\Omar.txt", "r")

# print(myFile)  # File Data Object بيانات عن الفايل
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read()) # تستخدم للقراء وتقبل عدد الحروف الذي تريد قرءتها
# print(myFile.read(37))

# print(myFile.readline()) # تستخدم لقراء سطر معين
# print(myFile.readline()) # لقراء السطر الذي بعده نعمل نقس الكود مره ثانيه بعده
# print(myFile.readline(5))

# print(myFile.readlines())  # تستخدم لقراء السطور كلها ويرجع لك ب List
# print(myFile.readlines(50))
# print(type(myFile.readlines()))

# for line in myFile:

#     print(line)

#     if line.startswith("07"):

#         break

# Close The File
# myFile.close() # تستخدم لغلق الملف بعد الانتهاء
# ? -------------------------------------- 067 ------------------------------------------------------
# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------
# @@ اذا لم بكن الملف موجود سوف يتم انشاء
# @@ عند استخدام نوع ال write يحذف العناصر الذي في الملف القديمة
# myFile = open("F:\Programing\Pyhton\Omar.txt", "w")
# myFile.write("Hello \n")
# myFile.write("Third Line")

# myFile = open(r"F:\Programing\Pyhton\fun.txt", "w")
# myFile.write("NTFS v6\n"*10)

# myList =["Omar\n","Ashraf\n","Gabl\n"]
# myFile = open(r"F:\Programing\Pyhton\Omar.txt", "w")
# myFile.writelines(myList)

# todo عند استخدام نوع ال Append يكتب العناصر الجديده علي العناصر الموجوده القديمه والملف اذا لم يكن موجود سوف يتم انشاء
# myFile = open(r"F:\Programing\Pyhton\fun.txt", "a")
# myFile.write("NTFS v6\n"*10)
# myFile.close()
# ? -------------------------------------- 068 ------------------------------------------------------
# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------
# import os
# print(os.getcwd())

# myFile = open("F:\Programing\Pyhton\Omar.txt", "a")
# myFile.truncate(5) #todo تستخدم لقص كلام او عدد معين من العناصر الموجوده داخل ال file ويحذف الباقي

# myFile = open("F:\Programing\Pyhton\Omar.txt", "a")
# print(myFile.tell()) #todo لمعرفه اين مؤشر الماوس ورقم المكان الذب هو به كام

# myFile = open("F:\Programing\Pyhton\Omar.txt", "a")
# myFile.seek(11) # todo يجعل الموس يذهب الي الرقم الذي تضعه بمعني اكنه بدا الكتابه من هذا المكان
# print(myFile.read())

# todo نستخدمها لحذف ملف او شي معين من خلال المسار بتاعه
# os.remove("F:\Programing\Pyhton\Omar.txt")

# myFile.close()
# ? -------------------------------------------------------------------------------------------- EX 068-065
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# import os
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# files_name = fr"c:\Users\omarb\OneDrive\Desktop\Python\assign.py"
# # files_name = files_name[-9:]

# print(files_name[-9:])

# file_num =1

# num = range(1, 51)

# for alls in num:

#     if alls == 25:

#         my_files = open(fr"c:\Users\omarb\OneDrive\Desktop\Python\special-text.txt","w")

#         my_files.close()

#     else:
#      my_files2 =open(fr"c:\Users\omarb\OneDrive\Desktop\Python\txt{alls}.txt","w")

#      my_files2.write(f"ElZero Web School => {alls}\n")

#      my_files2.close()

#     file_num +=1

# print(file_num)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# my_file = open(r"C:\Users\omarb\OneDrive\Desktop\Python\txt1.txt", "a")
# my_file.write("Appended => Elzero Web School\n"*50)
# my_file.close()
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# my_file = open(r"C:\Users\omarb\OneDrive\Desktop\Python\txt1.txt", "r")
# my_list = my_file.readlines()
# lines_num = len(my_list)
# words_num = 0
# chars_num = 0
# char_l_num = 0

# for x in my_list:

#     o = x.split()

#     words_num += len(x)

#     for i in x:

#         y = i.strip()

#         chars_num += len(y)

#         char_l_num += i.count("l")

# print(f"Number Of Lines Is => {lines_num}")
# print(f"Number Of Words Is => {words_num}")
# print(f"Number Of Chars Is => {chars_num}")
# print(f"Number Of \"l\" Char Is => {char_l_num}")

# my_file.close()
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# for i in range(41,51):
# os.remove(fr"C:\Users\omarb\OneDrive\Desktop\Python\txt{i}.txt")
# ? -------------------------------------- 069 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# todo all() تستخدم لمعرف هل كل العناصر صحيحه اذا كان عنصر واحد خطاء سيفو يرجع لك ب False
# todo any() تستخدم لمعرفه هل اي عنصر من العناصر صح ام هل كل العناصر خطاء
# todo bin() تستخدم لتحول اي شي الي binary للرقم الذي يفهمه الكمبيوتر 0-1
# todo id() يرجع لك بقيمه الشي الذي تم وضعه بداخل ذاكره الجهاز
# ------------------------

# x = [1, 2, 3, 4, []]

# if all(x):

#   print("All Elements Is True")

# else:

#   print("Theres At Least One Element Is False")

# x = [0, 0, []]

# if any(x):

#   print("There's At Least One Element is True")

# else:

#   print("Theres No Any True Elements")

# print(bin(100))

# a = 1
# b = 2

# print(id(a))
# print(id(b))
# print(id(3))
# ? -------------------------------------- 070 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# todo sum() تستخدم لجمع العناصر مع بعض الذي بداخل العنصر ويمكن الاضافه عليهم شيم عين يمكنك وضعه
# todo round() تستخدم لتقريب الرقم لاقرب قيمه عشريه
# todo range() تستخدم لوضع من رقم معين الي رقم معين اخر ويمكن تحديد رقم القفزه الواحده كام تساوي
# todo print("Hello", "Osama", sep=" $ ") عند استخدام كلمه sep ثم تضع اي شي تريده سوف يذيل الكومه ويضعه مكانه
# ------------------------
# sum(iterable, start)
# a = [1, 10, 19, 40]
# print(sum(a))
# print(sum(a, 30))

# round(number, numofdigits)
# print(round(150.501))
# print(round(150.555, 2))

# range(start, end, step)
# print(list(range(0)))
# print(list(range(10)))
# print(list(range(0, 20, 2)))

# print()
# print("Hello $ Osama $ How $ Are $ You")
# print("Hello", "Osama", "How", "Are", "You", sep=" $ ")

# todo عند استخدم كلمه end وتضع بداخلها اي قيمه سوف يجعل السطر الاول جنب الثاني واذا لم تفعل فان ال def value بتعتها هي \n
# print("First Line", end=" ## ")
# print("Second Line")
# print("Third Line")
# ? -------------------------------------- 071 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# todo abs() المسافه بين الصفر والرقم الذي سوف تضعه وترجع لك برقم موجب دئما
# todo pow() تستخدم لعمل عمليه حسابيه وهي الاوس وعند وضع قيمه اخر عنصر سوف يرجع لك بباقي القسمه بتاعت القسمه الاولي
# todo min() تستخدم لعرض اقل عنصر موجود
# todo max() تستخدم لعرض اعلي عنصر موجود
# todo slice() استخدمها الطبيعي كما تعلمنا في الدرس السابق ولكن هنا يوجد بدايه ونهايه
# ------------------------
# todo abs() بمعني صحيح يحذف السالب
# print(abs(100))
# print(abs(-100))
# print(abs(10.19))
# print(abs(-10.19))

# pow(base, exp, mod) => Power
# print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
# print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

# min(item, item , item, or iterator)
# myNumbers = (1, 20, -50, -100, 100)
# print(min(1, 10, -50, 20, 30))
# print(min("X", "Z", "Osama"))
# print(min(myNumbers))

# max(item, item , item, or iterator)
# myNumbers = (1, 20, -50, -100, 100)
# print(max(1, 10, -50, 20, 30))
# print(max("X", "Z", "Osama"))
# print(max(myNumbers))

# slice(start, end, step)
# a = ["A", "B", "C", "D", "E", "F"]
# print(a[:5])
# print(a[slice(5)])
# print(a[slice(2, 5)])
# ? -------------------------------------------------------------------------------------------- EX 071-069
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# values = (0, 1, 2)

# if any(values):
# any = اي عنصر من الذي بداخل المتغير
# will be True if any Element Is Ture ==> int,True,str,[element]

#     my_var = 0
# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
# وهنا بسبب استخدام ال or واول قيمه صحيحه فسوف يطبع لنا Good
# True if all Element is Ture in Range OR

#     print("Good")

# else:

#     print("Bad")
# all(my_list[:4]) => True
# output => good
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820

# for x in range(820):
#     if sum(list(range(x+1))) == 820:
#         print(x) # 40
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# n = 21
# n = round(22)

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#     print("Good")

# for x in range(1,100):
#     if round(sum(list(range(x)))/x) ==10:
#         print(x)
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# def my_all(*allos):
#     for x in allos:
#         if all(x) == all(allos):
#             return True
#         else:
#             return False
# ------
# def my_all(done):
#     d = 0
#     for r in done:
#         if bool(r):
#             d += 1
#     if d == len(done):
#         return True
#     else:
#         return False

# print(my_all([1, 2, 3]))  # True
# print(my_all([1, 2, 3, []]))  # False
# >-----------------------
# def my_any(*allos):
#     for x in allos:
#         if any(x) == any(allos):
#             return True
#         else:
#             return False
# -----
# def my_any(done):
#     d = 0
#     for r in done:
#         if bool(r):
#             d += 1
#     if d >= 1:
#         return True
#     else:
#         return False

# print(my_any([0, 1, [], False]))  # True
# print(my_any([(), 0, False]))  # False
# >-----------------------
# def my_min(*allos):
#     for x in allos:
#         if min(x) == min(x):
#             return f"{min(x)}"
# -----
# def my_min(allos):
#     k = allos[0]
#     for i in allos:
#         if i < k:
#             k = i
#     return k

# print(my_min([10, 100, -20, -100, 50]))  # -100
# print(my_min((10, 100, -20, -100, 50)))  # -100
# >-----------------------
# def my_max(*allos):
#     for x in allos:
#         if max(x) == max(x):
#             return f"{max(x)}"
# -----
# def my_max(allos):
#     k = allos[0]
#     for i in allos:
#         if i > k:
#             k = i
#     return k

# print(my_max([10, 100, -20, -100, 50, 700]))  # 700
# print(my_max((10, 100, -20, -100, 50, 700)))  # 700
# ? -------------------------------------- 072 ------------------------------------------------------
# -------------------------------
# -- Built In Functions => Map -- تستخدم لعمل loop
# -------------------------------
# [1] Map Take A Function + Iterator #@@ بتاخذ function و متغير
# [2] Map Called Map Because It Map The Function On Every Element #@@ ينفذ الكود علي جميع العناصر
# [3] The Function Can Be Pre-Defined Function or Lambda Function #@@ يتم تنفيذها علي function عاديه او lambda function
# ---------------------------------------------------------------
# Use Map With Predefined Function

# def formatText(text):

#   return f"- {text.strip().capitalize()} -"

# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# myFormatedData = map(formatText, myTexts)

# print(myFormatedData)

# for name in list(map(formatText, myTexts)):

#   print(name)

# Use Map With Lambda Function

# def formatText(text):

#   return f"- {text.strip().capitalize()} -"

# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

#   print(name)

# mu = range(1, 21)
# for my in list(map(lambda num: f"- {num}", mu)):
#     print(my)

# ? -------------------------------------- 073 ------------------------------------------------------
# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator #@@ بتاخذ function و متغير
# [2] Filter Run A Function On Every Element #@@ ينفذ الكود علي جميع العناصر
# [3] The Function Can Be Pre-Defined Function or Lambda Function #@@ يتم تنفيذها علي function عاديه او lambda function
# [4] Filter Out All Elements For Which The Function Return True #@@ عند تحقيق الهدف ب True يرجع لك بالقيمه غير ذالك يحذفه واكنه ليس متواجد
# [5] The Function Need To Return Boolean Value #@@ ترجع لك بقيمه False - True
# ---------------------------------------------------------------

# def checkNumber(num):

#     return num > 10

# myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

# myResult = filter(checkNumber, myNumbers)

# for number in myResult:

#     print(number)

#! Example 2-----

# def checkName(name):

#     return name.startswith("O")

# myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

# myReturnedData = filter(checkName, myTexts)

# for person in myReturnedData:

#     print(person)

#! Example 3-----

# myNames = ["Osama", "Omer", "Smar", "Ahmed", "Sayed", "Sound", "Ameer"]

# myReturnNames = filter(lambda name: name.startswith("S"), myNames)
# for p in myReturnNames:
# > ----------
# for p in filter(lambda name: name.startswith("S"), myNames):
#     print(p)

#! Example 4-----

# def num(nums):
#     return nums >= 10

# my_nums = range(1, 12)
# mynu = filter(num, my_nums)
# for nue in mynu:
#     print(nue)
# > ----------
# my_nums = range(1, 12)
# mynu = filter(lambda num: num >= 10, my_nums)
# for nue in mynu:

# for nue in filter(lambda num: num >= 10, my_nums):
#     print(nue)

# ? -------------------------------------- 074 ------------------------------------------------------
# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result #! تمجع اول عنصرين ثم ترجع لك بقيمه وتكمل الجمع علي باقي العناصر واحد وره التاني
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function #! ويمكن استخدام ال lambda function ايضا
# ---------------------------------------------------------------
# from functools import reduce

# def sumAll(num1, num2):

#   return num1 + num2

# numbers = [1, 8, 2, 9, 100]

# result = reduce(sumAll, numbers)

# result = reduce(lambda num1, num2: num1 + num2, numbers)

# print(result)

# ((((1 + 8) + 2) + 9) + 100)

# ? -------------------------------------- 075 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
#! enumerate() يعمل لك عداد ارقام بجانب ال العنصر المستخدم ويمكنك تحديد من كام يبداء
#! help() لمعرفه ما هي استخدمات ال Met او ال function وبيجبلك معلومات عنها
#! reversed() تستخدم لعكس وتغير مكان العنصر الي المكان المعكوس النحيه الثانية
# ------------------------
# enumerate(iterable, start=0)

# mySkills = ["Html", "Css", "Js", "PHP"]

# mySkillsWithCounter = enumerate(mySkills, 1)

# print(type(mySkillsWithCounter))

# for counter, skill in mySkillsWithCounter:

#     print(f" Your Skill Num {counter} Is {skill}")

# help()

# print(help(print))
# print(help(sum))

# reversed(iterable)

# myString = "Elzero"

# print(reversed(myString))

# for letter in reversed(myString):

#   print(letter)

# for s in reversed(mySkills):

#   print(s)
# ? -------------------------------------------------------------------------------------------- EX 075-072
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# def remove_chars(string):

#     return string[1:-1]

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list =map(remove_chars,friends_map)

# for i in map(remove_chars,friends_map):
#  print(i)

# cleaned_list =map(lambda string:string[1:-1],friends_map)
# for i in cleaned_list:
#  print(i)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# def get_names(name):
#     return name.endswith("m")

# fun_filter = filter(get_names, friends_filter)
# for m in filter(get_names, friends_filter):

# names = filter(lambda name: name.endswith('m'), friends_filter)
# for m in names:
# print(m)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# from functools import reduce
# def multiply(num1, num2):

#     return num1*num2

# nums = [2, 4, 6, 2]
# result = reduce(multiply, nums)
# print(reduce(multiply, nums))
# result = reduce(lambda num1 ,num2:num1*num2, nums)
# print(result)
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# skills = reversed(skills)

# skills = enumerate(skills, 50)

# skills= list(skills)

# def cleaner(name):

#     if type(name[1])==int:

#      pass

#     else:

#         return name

# cleaned = filter(cleaner,skills)

# for i,s in cleaned:

#     print(f"{i} - {s}")

# cleaner(skills)
# -----------------------
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# skills = reversed(skills)

# skills = enumerate(skills, 50)

# skills= list(skills)

# for x,y in skills:
#     if type(y)==int:
#         continue
#     else:
#         print(f"{x} - {y}")
# -----------------------
# names = ["AShraf", "Nite", "Fight", "Omar"]
# names = enumerate(names,0)
# for i,n in names:
#     print(f"Index {i} => {n}")

# Index 0 => AShraf
# Index 1 => Nite
# Index 2 => Fight
# Index 3 => Omar
# -----------------------
# names = ["AShraf", "Nite", 25, "Fight", 15, "Omar"]

# def del_num(name):

#     for i in names:

#         if type(i) == int:

#             continue

#         name = enumerate(name, 0)

#         for n, m in name:

#             print(f"Index Is {n} Element => {m}")

# del_num(names)
# -----------------------
# def formatText(text):

#     return f"- {text.strip().capitalize()} -"

# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# nums = list(map(formatText, myTexts))

# nums=list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts))

# for name in nums:

#     print(name)
# -----------------------
# ? -------------------------------------- 076 ------------------------------------------------------
# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------
# Import Main Module
# import random # نستخدم import لاستدعاء شي معين وعلي حسب ما نحتاج
# print(random) #! لمعرفة مكان الشي الذي تم استدعاءه في الجهاز
# print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
# print(dir(random)) #! لمعرفه جميع العناصر الذي بداخل الشي الذي تم استدعاء نستخدم dir()

# Import One Or Two Functions From Module
# todo نستخدم كلمه From ثم اسم الشي الذي نريد استدعاءه ثم import * تعني جميع عناصر الشي الذي تم استدعاءه
# from random import *
# todo لااستدعاء عنصر واحد فقط باستخدام اسمه وعلي حسب ماذا تريد ايضا form اسم ال Module ثم import اسم ال function
# from random import randrange
# todo ويمكننا اتستدعاء 2 function مع بعض بشكل عادي نفس فكره الثانية
# todo لااستدعاء عنصر واحد فقط باستخدام اسمه وعلي حسب ماذا تريد ايضا form اسم ال Module ثم import اسم ال function
# from random import randint, random
# print(f"Print Random Float {random()}")
# print(f"Print Random Integer {randint(100, 900)}")
# ? -------------------------------------- 077 ------------------------------------------------------
# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------
# import sys
# print(sys.path) #todo نستخدم module sys ثم path لمعرفه مسارات جميع ملفات البايثون الذي علي الجهاز
# sys.path.append(r"F:\test") #todo لاضافت مسار جديد لمكان ال module الجديد
# print(sys.path)

# import module
# print(dir(module)) # لمعرفه مسار الملف

# module.sayHello("Ahmed")
# module.sayHello("Osama")
# module.sayHello("Mohamed")

# module.sayHowAreYou("Ahmed")
# module.sayHowAreYou("Osama")
# module.sayHowAreYou("Mohamed")

# Alias

# import module as mo
#! لعمل اسم مستعار لل module او ال function الذي سوف نستدعيها نستخدم as ثم الاسم المستعار
# print(dir(module))

# mo.say_hello("Omar")
# mo.say_hello("Omar")
# mo.say_hello("Omar")

# mo.say_name("Omar")
# mo.say_name("Omar")
# mo.say_name("Omar")

# from module import say_hello

# say_hello("Osama")

# from module import say_hello as ss #todo لعمل اسم مستعار لل function نستخدم نفس الشي

# ss("Osama")
# ? -------------------------------------- 078 ------------------------------------------------------
# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# >--------------------------------------------------------------------------------------------------------
# Command line for get Package
# >--------------------------------------------------------------------------------------------------------
#! نستخدم pip لان هذه هي المسؤله عن جميع المكتبات الذي بداخل لغه Python
#! pip list لمعرفه جميع المكتبات الذي تم تحملها وجميع اصدرتها
#! pip --verison
#! pip install اسم المكتبه
#! مثال pip install pyfiglet هذه مكتبه بمكن ان نستخدم منها اشياء كثيره
#! pip install pyfiglet==verison يمكن ان نعمل تحميل ل verison معين من خلال ان نضع رقم ال verison بعد ال == او هذا ال verison او اكبر من خلال >=
#! مثال pip install pyfiglet>=1.0
# ---------------------------------------------------------------------
# import termcolor
# import pyfiglet

# print(dir(pyfiglet))
# print(pyfiglet.figlet_format("omar"))
# print(help(termcolor))

# print(sys.path)
# print(termcolor.colored(pyfiglet.figlet_format("omar"),"red"))
# print(termcolor.colored('Hello, World!', 'green'))

# @@ نستخدم function figlet_format لتكبير الخط وتذينه بشكل كبير
# @@ نستخدم function colored لعمل لون لكلمه او شي معين
# ? -------------------------------------------------------------------------------------------- EX 078-076
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# import random
# print(f"Random Number Between 10 And 50 => {random.randint(10,50)} ")
# >--------------------------------
# rand = random.randint(2, 10)
# if rand == 3 or rand == 5 or rand == 7 or rand == 9:
#     pass
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
# ? -------------------------------------- 079 ------------------------------------------------------
# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------
# نستدعي مكتبه الوقت
# import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
# print(datetime.datetime.now()) #! لطباعة الوقت الحالي بجميع انواعة
# print(datetime.datetime.today())

# Print The Current Year
# print(datetime.datetime.now().year) #@@ لطباعة السنه فقط

# # Print The Current Month
# print(datetime.datetime.now().month) #@@ لطباعة الشهر فقط

# # Print The Current Day
# print(datetime.datetime.now().day) #@@ لطباعة اليوم فقط

# todo بدايه ونايه التاريخ
# # Print Start and End Of Date
# print(datetime.datetime.min) #@@ لطباعة اول وقت تم
# print(datetime.datetime.max) #@@ لطباعة اخر وقت تم

# print(dir(datetime.datetime.now()))

# ? لطباعة الوقت الحالي علي حسب ماتريد
# # Print The Current Time
# print(datetime.datetime.now().time())

# # Print The Current Time Hour
# print(datetime.datetime.now().time().hour)

# # Print The Current Time Minute
# print(datetime.datetime.now().time().minute)

# # Print The Current Time Second
# print(datetime.datetime.now().time().second)

# # Print The Current Time Microsecond
# print(datetime.datetime.now().time().microsecond)

# todo بدايه ونهايه الوقت العاديه
# # Print Start and End Of Time
# print(datetime.time.min)
# print(datetime.time.max)

# todo لعمل وقت مخصص لك انت علي حسب ما تكبته
# # Print Specific Date
# print(datetime.datetime(2000, 10, 25))
# print(datetime.datetime(2000, 10, 25, 10, 45, 55, 150364))

# myBirthDay = datetime.datetime(2000, 6, 30)
# dateNow = datetime.datetime.now()

# print(datetime.datetime.now())

# print(f"My Birthday is {myBirthDay} ", end="And ")
# print(f"Date Now Is {dateNow}")

# print(f" I Lived For {dateNow - myBirthDay}")
# print(f" I Lived For {(dateNow - myBirthDay).seconds} Seconds.")
# print(f" I Lived For {(dateNow - myBirthDay).days} Days.")

# ? -------------------------------------- 080 ------------------------------------------------------
# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------
# import datetime

#! نستخدم function strftime لترجع لك ب String

# @@ عند استخدمها يوجد بعض الرموز الذي تطبع لك شي معين كالتالي وجميعها علي موقع باسم
# ? https://strftime.org/

# %a	Sun	Weekday as locale’s abbreviated name.
# %A	Sunday	Weekday as locale’s full name.
# %w	0	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %d	08	Day of the month as a zero-padded decimal number.
# %-d	8	Day of the month as a decimal number. (Platform specific)
# %b	لطباعة الشهر ب3 حروف Aug
# %B	لطباعه الشهر بشكل كامل August
# %m	09	Month as a zero-padded decimal number.
# %-m	9	Month as a decimal number. (Platform specific)
# %y	13	Year without century as a zero-padded decimal number.
# %Y	2013	Year with century as a decimal number.
# %H	07	Hour (24-hour clock) as a zero-padded decimal number.
# %-H	7	Hour (24-hour clock) as a decimal number. (Platform specific)
# %I	07	Hour (12-hour clock) as a zero-padded decimal number.
# %-I	7	Hour (12-hour clock) as a decimal number. (Platform specific)
# %p	AM	Locale’s equivalent of either AM or PM.
# %M	06	Minute as a zero-padded decimal number.
# %-M	6	Minute as a decimal number. (Platform specific)
# %S	05	Second as a zero-padded decimal number.
# %-S	5	Second as a decimal number. (Platform specific)
# %f	000000	Microsecond as a decimal number, zero-padded on the left.
# %z	+0000	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
# %Z	UTC	Time zone name (empty string if the object is naive).
# %j	251	Day of the year as a zero-padded decimal number.
# %-j	251	Day of the year as a decimal number. (Platform specific)
# %U	36	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
# %W	35	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.

# print(datetime.datetime.now().strftime("%b"))
# print(datetime.datetime.now().strftime("%B"))

# myBirthday = datetime.datetime(2000, 6, 30)

# print(myBirthday)

# print(myBirthday.strftime("%a"))
# print(myBirthday.strftime("%A"))
# print(myBirthday.strftime("%b"))
# print(myBirthday.strftime("%B"))

# print(datetime.datetime.now().strftime("%d %B %Y"))

# @@ لطباعة اليوم والشهر والسنه بكشل افضل
# print(myBirthday.strftime("%d %b %Y"))
# print(myBirthday.strftime("%d, %B, %Y"))
# @@ ويمكننا وضع ما نريد واي كلام ف النصف بشكل طبيعي
# print(myBirthday.strftime("%d/%B/%Y"))
# print(myBirthday.strftime("%d - %B - %Y"))
# print(myBirthday.strftime("Born In %d And Month %B And Year Is %Y"))
# print(myBirthday.strftime("%B - %Y"))
# ? -------------------------------------------------------------------------------------------- EX 080-079
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# import datetime

# myDate = datetime.datetime(2021, 6, 25)
# myDate2 = datetime.datetime(2021, 8, 10)
# print(f"Days From 2021-06-25 To 2021-08-10 Is => {(myDate2-myDate).days} Days.")
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# dateNow = datetime.datetime(2021, 8, 10)

# print(dateNow.strftime("%Y-%m-%d")) # 2021-08-10
# print(dateNow.strftime("%b %d, %Y")) # "Aug 10, 2021"
# print(dateNow.strftime("%d - %b - %Y")) # "10 - Aug - 2021"
# print(dateNow.strftime("%d / %b / %y")) # "10 / Aug / 21"
# print(dateNow.strftime("%d / %B / %Y")) # "10 / August / 2021"
# print(dateNow.strftime("%a, %d  %B  %Y")) # "Tue, 10 August 2021"
# ? -------------------------------------- 081 ------------------------------------------------------
# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# @@ هو اللوب العادي الذي نعمله
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# @@ هو لوب ولكن بشكل اخر وراء الكواليس باستخدام Method next()
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# @@ ونستخدم Method iter() وهذه الماسوس هي الذي تعمل اللوب
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------
# myString = "Osama"

# myList = [1, 2, 3, 4, 5]

# for letter in myString:

#     print(letter, end=" ")

# for number in myList:

#     print(number, end=" ")

# myIterator = iter(myString)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# --
# for letter in "Elzero":

#     print(letter, end=" ")
# --
# for letter in myList:

#     print(letter, end=" ")
# --
# for letter in iter("Elzero"):

#     print(letter, end=" ")
# --
# for letter in iter(myString):

# print(letter, end=" ")
# print(letter)
# ? -------------------------------------- 082 ------------------------------------------------------
# ----------------
# -- Generators --
# ----------------
# @@ عند استخدام ال yield يمكنك طباعة العنصر في الوقت المناسب لك علي حسب ما تريد ويمكنك عمل loop ايضا ويوجد بعض المميزات كالتالي
# @@ ال yield زيها زي ال return ولكن تستخدم لطباعه شي معين ف الوقت الذي تريده
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# @@ تدعم استخدام ال Iteration + Iterator من خلال ال yield
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# @@ يمكن استخدام العديد من ال yield بشكل عادي بدون اي مشاكل
# [3] Generator Function Can Have one or More "yield"
# @@ ويمكن استخدام ال next() لطباعه ال yield خلف بعض او يمكن طباعه شي معين ف النصف ثم تعمل باقي العمليه
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# @@ عند البدايه لا يبداء تلقائي انت المسؤال عن البدايه والنهايه وما بالمنتصف
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------
# name="Sona"
# def myGenerator():
#     yield "Omar"
#     yield name
#     yield 3
#     yield 4

# myGen = myGenerator()

# print(f"Hello {next(myGen)} From Welcome In Programing")
# print(next(myGen))
# print("Hello From Python")
# print(next(myGen))
# print("Hello From Python")
# print(next(myGen))
# print("Hello From Python")

# for number in myGen:
#     print(number)
# > -----------------
# def myGenerator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# myGen = myGenerator()

# print(next(myGen))
# print("Hello From Python")
# print(next(myGen))

# for number in myGen:
#     print(number)
# ? -------------------------------------- 083 ------------------------------------------------------
# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
# def myDecorator(func):  # Decorator

#     def nestedFunc():  # Any Name Its Just For Decoration

#         print("Before")  # Message From Decorator

#         func()  # Execute Function

#         print("After")  # Message From Decorator

#     return nestedFunc  # Return All Data

# @myDecorator  # B~ نستخدمها للمناده علي ال function الام
# def sayHello():

#     print("Hello From Say Hello Function")


# @myDecorator  # B~ نستخدمها للمناده علي ال function الام
# def sayHowAreYou():

#     print("Hello From Say How Are You Function")

# afterDecoration = myDecorator(sayHello) # @@ هذه شكل ال devorator الطبيعي
# afterDecoration1 = myDecorator(sayHowAreYou) # @@ هذه شكل ال devorator الطبيعي

# afterDecoration() #@@ ثم ننادي عليه هنا بشكل عادي
# sayHello()  # ! بعد المناده علي function الام نستجعي ال function الذي سوف نستخدمها بشكل عادي

# sayHowAreYou() # ! بعد المناده علي function الام نستجعي ال function الذي سوف نستخدمها بشكل عادي
# afterDecoration1() #@@ ثم ننادي عليه هنا بشكل عادي
# ? -------------------------------------- 084 ------------------------------------------------------
# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------
# def myDecorator(func):  # Decorator

#   def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

#     if num1 < 0 or num2 < 0:

#       print("Beware One Of The Numbers Is Less Than Zero")

#     func(num1, num2)  # Execute Function

#   return nestedFunc  # Return All Data
# >--------------------------------------------
# def myDecoratorTwo(func):  # Decorator

#   def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

#     print("Coming From Decorator Two")

#     func(num1, num2)  # Execute Function

#   return nestedFunc  # Return All Data

# @myDecorator #@@ يمكننا المناده علي 2 function الام لنفس ال function المستهدفه
# @myDecoratorTwo #@@ يمكننا المناده علي 2 function الام لنفس ال function المستهدفه

# def calculate(n1, n2):

#   print(n1 + n2)

# calculate(-5, 90)
# ? -------------------------------------- 085 ------------------------------------------------------
# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------
# from time import time

# def myDecorator(func):  # Decorator

#     def nestedFunc(*numbers):  # Any Name Its Just For Decoration

#         for number in numbers:

#             if number < 0:

#                 print("Beware One Of The Numbers Is Less Than Zero")

#         func(*numbers)  # Execute Function

#     return nestedFunc  # Return All Data

# @myDecorator
# def calculate(n1, n2, n3, n4):

#     print(n1 + n2 + n3 + n4)

# calculate(-5, 90, 50, 150)

# def speedTest(func):

#     def wrapper():

#         start = time()

#         func()

#         end = time()

#         print(f"Function Running Time Is: {end - start}")

#     return wrapper

# @speedTest
# def bigLoop():

#     for number in range(1, 200):

#         print(number)

# bigLoop()
# ? -------------------------------------------------------------------------------------------- EX 085-081
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
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
# def reverse_string(my_string):
#     for n in my_string:
#         yield n

# for c in reverse_string("Elzero"):
#     print(c)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# def Deco(func):
#     def nestFun(*any):

#         print("Sugar Added From Decorators")

#         func(*any)

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
# ? -------------------------------------- 086 ------------------------------------------------------
# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------
# list1 = [1, 2, 3, 4, 5]
# list2 = ["A", "B", "C", "D","N"]
# tuple1 = ("Man", "Woman", "Girl", "Boy", "Friend")
# dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python","Stuuf":"Null"}

# for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

#     print("List 1 Item =>", item1)
#     print("List 2 Item =>", item2)
#     print("Tuple 1 Item =>", item3)
#     print("Dict 1 Key =>", item4, "=>", dict1[item4])

# ultimateList = zip(list1, list2)
# for item in ultimateList:
#     print(item)
# ? -------------------------------------- 087 ------------------------------------------------------
# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# ? https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
# -------------------------------------------------
# todo تم استدعاء مكتبه تعديل الصور ومن خلاللها استدعينا function Image
# from PIL import Image

# Open The Image
#! هنا عوان الصوره وفتحها بكشل عادي
# myImage = Image.open("F:\Programing\Pyhton\img.jpg")

# Show The Image
# myImage.show()  # ! نستخدم ال show() لعرض الصوره

# My Cropped Image
# todo هنا تم استخدام ابعاد معينه لقص الصوره بالشكل الذي تريده
# myBox = (300, 300, 800, 800)
# todo تم استخدام .crop لتطبيق الابعاد الذي سوف تقصها من الصوره
# myNewImage = myImage.crop(myBox)

# Show The New Image
# myNewImage.show()

# My Converted Mode Image
# ! تم استخدام convert("L") لتحويل الصوره الي ابض واسود
# myConverted = myImage.convert("L")
# myConverted.show()
# ? -------------------------------------- 088 ------------------------------------------------------
# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and __doc__ Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# todo نستخدمها لشرح كود معين ماذا يفعل
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------
# def elzero_function(name):
# todo ''' doc commenting''' # لكتابه كومنت علي سطر واحد

#   """ #todo لكتابه كومنت علي اكثر من سطر
#   Elzero Function
#   It Say Hello From Elzero
#   Parameter:
#     name => Person Name That Use Function
#   Return:
#     Return Hello Message To The Person
#   """
# print(f"Hello {name} From Elzero")

# elzero_function("Ahmed")

# print(dir(elzero_function))

# ! لمعرفه ما هو الكومنت المكتوب نستخدم اسم ال function.__doc__
# print(elzero_function.__doc__)

# ! لمعرفه الكومنت المكتوب نستخدم ايضا help(اسم ال function)
# help(elzero_function)
# ? -------------------------------------- 089 ------------------------------------------------------
# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# pylint.exe (name file)
# -----------------------------------------------
# """
# This is My Module
# To Crate Function
# To Say Hello
# """
# ! للمناده علي المكتبه الذي تعدل الكود او تساعدك علي كتابه كود نظيف نستخدم هذا الامر في ال TERMINAL
# @@ pylint.py ثم Name File الذي تستخدمه
# @@ pylint.exe f:/Programing/Pyhton/python/main.py

# def say_hello(name):
#     ''' Use For Say Hello In Function'''
#     msg = "Hello"
#     print(f"{msg} {name}")

# say_hello("Omar")

# ? -------------------------------------------------------------------------------------------- EX 089-086
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# n = 0
# for data in zip(my_list, my_tuple):
#     my_data.append(data)
#     final_string = f" {my_data}".replace(
#         "(", "").replace("'", "").replace(")", "").replace(
#             ",", "").replace(" ", "").replace("[", "").replace("]", "").capitalize()

# print(final_string)  # Elzero
# >--------
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list,my_tuple):
#     my_data.extend(data)
# final_string=("".join(my_data)).capitalize()
# print(final_string)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     if type(item1) == str:
#       my_data.append(item1)
#       final_string = f" {my_data}".replace(
#         "(", "").replace("'", "").replace(")", "").replace(
#             ",", "").replace(" ", "").replace("[", "").replace("]", "").capitalize()
# print(final_string)
# >---------
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
# myrotate= myConverted2.rotate(180)
# myNewImage2.show()
# myConverted2.show()
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
# '''This For List Name Pepole'''
# my_friends = ["Ahmed","Osama","Sayed"]
# """MAke Function To Type names for List"""
# def say_hello(some_peoples) -> list:
#     '''Function To Type List Names'''
#     for some_one in some_peoples:
#         print(f"Hello {some_one}")
# say_hello(my_friends)
# ? -------------------------------------- 090 ------------------------------------------------------
# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# @@  وهذا موقع به جميع انواع اسماء ال ERROR
# J$ [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# B~ raise تستخدم لطباعه ال ERROR COde ثم بعدها نوع ال ERROR الذي تريد طباعته
# @@ raise NameError (----)
# @@ raise Exception ("FIx Your ERROR FROm HERE")
# -----------------------------------------------------------------
# x = -10

# if x < 0:

#   raise Exception(f"The Number {x} Is Less Than Zero")

#   print("This Will Not Print Because The Error")

# else:

#   print(f"{x} Is Good Number and Ok")

# print('Print Message After If Condition')

# y = "S"

# if type(y) != int:

#     raise ArithmeticError("Only Numbers Allowed")

# print('Print Message After If Condition')
# ? -------------------------------------- 091 ------------------------------------------------------
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------
# number = int(input("Write Your Age: "))

# print(number)
# print(type(number))

# try:  # Try The Code and Test Errors
#   number = int(input("Write Your Age: "))

# # @@ عند كتابه رساله معينه هنا سوف يتم طباعتها اذا لم يتواجد ERROR ايضا وهنا افضل من ال else
#   print("Good, This Is Integer From Try")

# except:  # Handle The Errors If Its Found
#   print("Bad, This is Not Integer")

# # @@ نستخدم ال else لكي اذا لم يتواجد ERROR يطبع لك رساله
# else:  # If Theres No Errors
#   print("Good, This Is Integer From Else")

# # @@ نستخدم ال finally اذا وجد ERROR او لم يجد ERROR سوف يطبع لك الرساله بكل الطرق سوف تطبع
# finally:
#   print("Print From Finally Whatever Happens")
# >----------------------------------------------------
# >----------------------------------------------------
# @@ عند استخدام هذا الشكل اذا لم يجد ERROR سوف يطبع اول رساله موجوده ف ال try
# try:
#     print(10 / 0)
#     print(x)
#     print(int("Hello"))
# >---------
#     print(10+1)
#     print("Nice Code Keep Going")

# # @@ اذا وجد ERROR بنوع ZeroDivisionError سوف يطبع لك هذه الرساله
# except ZeroDivisionError:
#     print("ERROR FroM ZeroDivisionError")

# # @@ اذا وجد ERROR بنوع NameError سوف يطبع لك هذه الرساله
# except NameError:
#     print("ERROR FroM NameError")

# # @@ اذا وجد ERROR بنوع ValueError سوف يطبع لك هذه الرساله
# except ValueError:
#     print("ERROR FroM ValueError")

# # @@ اذا وجدت اي نوع ERROR اخر اطبع الرساله دي
# except:
#     print("ERROR For Any Value")
# ? -------------------------------------- 092 ------------------------------------------------------
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
# the_file = None

# the_tries = 5

# while the_tries > 0:

#     try:  # Try To Open The File
#         print("Enter The File Name With Absolute Path To Open")

#         print(f"You Have {the_tries} Tries Left")

#         print("Example: F:\Programing\Pyhton\yourfile.extension")

#         file_name_and_path = input("File Name => : ").strip()

#         the_file = open(file_name_and_path, "r")

#         print(the_file.read())

#         break
#     except FileNotFoundError:
#         print("File Not Found Please Be Sure The Name is Valid")

#         the_tries -= 1

#     except:
#         print("Error Happen")

#     finally:
#         if the_file is not None:

#             the_file.close()

#             print("File Closed.")
# else:
#     print("All Tries Is Done Please Try Again")
# ? -------------------------------------- 093 ------------------------------------------------------
# --------------------
# -- Debugging Code --
# @@ نستخدم ال Debugging لكي اذا كان في ERROR في كود ولا تعرف ما هو الكود الذب به ال ERROR ال Debugging يكشف لك كل هذه بكل بساطه
# @@ نضع بجانب الكود المشكوك به العلامه الحمرا لكي نرا ال Debugging الذي سوف يحدث عليه
# --------------------
# my_list = [1, 2, 3]

# my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

# for num in my_list:

#   print(num)

# for key, value in my_dictionary.items():

#   print(f"{key} => {value}")

# def function_one_one():

#   print("Hello From Function One")

# function_one_one()
# ? -------------------------------------- 094 ------------------------------------------------------
# ------------------
# -- Type Hinting --
# @@ تكون عباره عن ملاحظه بسيطه لتقول للذي امماك ان نوع البيانات هو كذا
# B~ ال function() -> نوع البيانات
# B~ function()  -> str
# ------------------
# def say_hello(name) -> str:
#     # def say_hello(name) -> True:

#     print(f"Hello {name}")

# say_hello("Ahmed")

# def calculate(n1, n2) -> int or str:

#     print(n1 + n2)

# calculate(10, 40)
# ? -------------------------------------------------------------------------------------------- EX 094-090
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
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
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
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
# ? -------------------------------------- 095 ------------------------------------------------------
# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# -----------------------------------------------------------
# ? -------------------------------------- 096 ------------------------------------------------------
# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# B~ WebSite =>> https://regex101.com/
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# -------------
# ? -------------------------------------- 097 ------------------------------------------------------
# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# Hello Im try_ElDeep from Learing Python
# My Number Is 1545842515 s55w
# My Email eldeep@sona.net
# 123123123 123456 15288152
# -----------------------------------------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# ? -------------------------------------- 098 ------------------------------------------------------
# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$

# omareldeeproot125@gmail152.com
# fak23omareldeeprougfbuaot1dadqwpk12o25@gmail152.net
# omareldeeproot125@gmail152.set
# ? -------------------------------------- 099 ------------------------------------------------------
# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# -----------------------------
# (\d-|\d\)|\d>) (\w+)
# 1- Sona
# 1) Nile
# 1> goos

# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# 123 1258 952
# 123 1258 (952)

# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$
# https://www.nileDeep.com
# https://sonanileDeep.org
# https://nileDeep.me
# http://nileDeep.net
# ? -------------------------------------- 100 ------------------------------------------------------
# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------
# import re

# my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

# print(my_search)
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())

# ! نستخدم ال re.search لعمل ال Regular in python وتستخدم للبحث في عناصر معينه
# is_mail = re.search(
#     r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "sona15@gmaik.com")

# if is_mail:
#     print(f"Your Mail Span => {is_mail.span()}")
#     print(f"Your Mail Is => {is_mail.group()}")
#     print(f"Your Mail Is => {is_mail.string}")
# else:
#     print("Type Your Mail True")

# email_input = input("Please Write Your Email: ")

#! نستخدم نوع ال findall للبحث في جميع العناصر مره واحده غير ال search
# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

# empty_list = []

# if search != []:

#     empty_list.append(search)

#     print(f"Your Email Added")

# else:

#     print("Invalid Email")

# for email in empty_list:

#     print(email)
# ? -------------------------------------- 101 ------------------------------------------------------
# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------
# import re

# string_one = "I Love Python Programming Language"

# search_one = re.split(r"\s", string_one, 1)

# print(search_one)

# print("#" * 50)

# string_two = "How-To_Write_A_Very-Good-Article"

# search_two = re.split(r"-|_", string_two)

# print(search_two)

# Get Words From URL

# for counter, word in enumerate(search_two,1):

#   if len(word) <= 1:

#     continue

#   print(f"Word Number: {counter} => {word.lower()}")

# print("#" * 50)

# my_string = "I Love Python"

# @@ هذه مثل ال replace تبدل شي معين بشي اخر ويمكنك وضع حد لفعل هذه بشكل طبيعي
# print(re.sub(r"\s", "-", my_string, 1))
# ? -------------------------------------- 102 ------------------------------------------------------
# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------
# import re

# my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

#! يتم كتابه ال flag بهذا الشكل بكل سهوله
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web,re.MULTILINE)
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web,re.IGNORECASE)
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web,re.DOTALL)
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web,re.VERBOSE)

# print(search.group())
# print(search.groups())

# for group in search.groups():

#   print(group)

# print(f"Protocol: {search.group(1)}")
# print(f"Sub Domain: {search.group(2)}")
# print(f"Domain Name: {search.group(3)}")
# print(f"Top Level Domain: {search.group(4)}")
# print(f"Port: {search.group(5)}")
# print(f"Query String: {search.group(6)}")
# ? -------------------------------------------------------------------------------------------- EX 102-095
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# eeeeE llllLl lllzzZzzzz eroe operationr pollo =>> (\w\s)
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111 =>> [G-L](Elzero)
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234 ====>>>> (\+?\([0-9]{4}\)? [0-6]{2,4}?-[0-4]{4})
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py         =>>>> # (https?)://(www)?\.?(\w+)\.(com|org):?(\d+)?/?(\w+)\.(php|py)
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# https?
# [h-z]
# [h-z]{4,5}
# [f-z]
# [^ab-d]
# >--
# http
# https
# abcd
# abcd
# ? -------------------------------------- 103 ------------------------------------------------------
# ------------------------------------------
# -- Object Oriented Programming => Intro --
#! تستخدم لجعل الكود بكل سلسة واكثر فعاليه ويوجد منه انواع
# ------------------------------------------
# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
#     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
#     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#     - Methods[Behaviors] => Walking, Stopping
# [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object
# ---------------------------------------------
# ? -------------------------------------- 104 ------------------------------------------------------
# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
#! ال class تكون عباره عن مخطط الي من عن طريقه نقدر ننشاء المشروع الخص بينا
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
#! يتم انشاء من ال class ال instance وهذا عباره عن ال object الي انت بتنشاء من ال class وتاخد منه ال Methods + Attributes
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
#! يمكننا استخدام ال class من خلال استخدام كلمه class
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
#! يمكن ال class بتاعك يحتوي علي Methods and Attributes وممكن لا
# [06] Class May Contains Methods and Attributes
#! لمه بتنشاء object جديد لغه بايثون بتدور علي حاجه اسمها  __init__ ويتم منادتها كل لحظه انت بتنشاء في ال object من ال class المستخدمه
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
#! تستخدم لتهياء الداته لل object الذي سوف يتم انشاءه
# [09] __init__ Method Is Initialize The Data For The Object
#! اي شي في لغه بايثون يبداء ب __name__ يسمي ال Dunder or Magic Method
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
#! يستحسن يكون اول براميتر عند انشاء ال class
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
#! ويمكن تسميته ب اي اسم عادي جدا
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------
# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function
#! يتم عمل ال class بهذا الشكل نستخدم كلمه class ثم اسمها
# class Member:
#! وهنا تم عمل function وتم استخدامها باسم (self)
#   def __init__(self):

#     print("A New Member Has Been Added")
#! للمناده علي ال class واستخدمه بشكل عادي ننده علي اسم ال class
# Member()
# member_one = Member()
# member_two = Member()
# member_three = Member()

# print(member_one.__class__)
# ? -------------------------------------- 105 ------------------------------------------------------
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
#! ال Attributes الخاصه بال Instance بتكون داخل ال Constructor البناء
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
# class Member:

#! يمكننا وضع اكثر من نوع بيانات وتغيره علي حسب اسم الشخص الذي سوف يتسخدم ال class
#     def __init__(self, first_name, middle_name, last_name):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name

# member_one = Member("Osama", "Mohamed", "elsayed")
# member_two = Member("Ahmed", "Ali", "Mahmoud")
# member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)
# ? -------------------------------------- 106 ------------------------------------------------------
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
# class Member:

# ^^ self هنا تعود علي اسم ال Instance ويمكن تغير اسمها بشكل عادي جدا وبجانبها اي متغير تريد وضعه ويتغير قمته علي حسب الادخال الذي يضعه المستخدم
# def __init__(self, first_name, middle_name, last_name, gender):
# ^^ الذي يتم كتابته هنا يكون غير الي مكتوب بره والفرق ان هنا بداخل ال Instance وبره في ال class

# ^^ لعمل ال Methods بشكل داينامك نستدعي ال self. اسم ال Methods = قيمه ال  Methods الذي سوف تضعها حين النده عليها
#     self.fname = first_name
#     self.mname = middle_name
#     self.lname = last_name
#     self.gender = gender

# def full_name(self):
#     return f"{self.fname} {self.mname} {self.lname}"

# def name_with_title(self):
#     if self.gender == "Male":
#         return f"Hello Mr {self.fname}"
#     elif self.gender == "Female":
#         return f"Hello Miss {self.fname}"
#     else:
#         return f"Hello {self.fname}"

# def get_all_info(self):

# ^^ ويمكننا دمج اكثر من Methods مع بعض بهذا الشكل لان كلهم مفتحوين ع بعض بشكل عادي جدا
# return f"{self.name_with_title()}, Your Full Name Is => {self.full_name()}"

#! هذه قيمه ال methods وطبعا لا نحسب ال self منهم نستعدي اسم ال class ثم متغيرات ال methods
# member_one = Member("Omar", "Ashraf", "ElDeep", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

# print(member_one.get_all_info())
# print(member_three.get_all_info())
# ?--------------------------------
# class test:

#     def __init__(self, name, age, gender):

#         self.name = name
#         self.age = age
#         self.gender = gender

#         print(
#             f"Hello {self.name} Your Age => {self.age} And Your {self.gender}")

#     def fix_all(self):

#         if self.gender == "Male":

#             return f"Hello Mr {self.name}"

#         elif self.gender == "Female":

#             return f"Hello Miss {self.name}"

#         else:
#             return f"Hello {self.name}"

# msg_hello = test("RooT", 22, "Male")
# msg_hello1 = test("Salma", 20, "Female")
# msg_hello2 = test.fix_all(omar("SoNa", 22, "Male"))
# msg_hello3 = msg_hello.fix_all()
# msg_hello4 = msg_hello1.fix_all()
# print(msg_hello2)
# print(msg_hello3)
# print(msg_hello4)
# ? -------------------------------------- 107 ------------------------------------------------------
# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------
# class Member:

# ^^ الذي يتم انشاءه هنا يكون بداخل ال class ليس بداخل ال Instance
#   not_allowed_names = ["Hell", "Shit", "Baloot"]

#   users_num = 0

#   def __init__(self, first_name, middle_name, last_name, gender):

#     self.fname = first_name

#     self.mname = middle_name

#     self.lname = last_name

#     self.gender = gender

#     Member.users_num += 1  # Member.users_num = Member.users_num + 1

#   def full_name(self):

#     if self.fname in Member.not_allowed_names:

#       raise ValueError("Name Not Allowed")

#     else:

#       return f"{self.fname} {self.mname} {self.lname}"

#   def name_with_title(self):

#     if self.gender == "Male":

#       return f"Hello Mr {self.fname}"

#     elif self.gender == "Female":

#       return f"Hello Miss {self.fname}"

#     else:

#       return f"Hello {self.fname}"

#   def get_all_info(self):

#     return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#   def delete_user(self):

#     Member.users_num -= 1  # Member.users_num = Member.users_num -1

#     return f"User {self.fname} Is Deleted."

# print(Member.users_num)

# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)

# print(member_four.delete_user())

# print(Member.users_num)

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

# print(member_three.get_all_info())

# print(dir(Member))
# ? -------------------------------------- 108 ------------------------------------------------------
# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# C% @classmethod
# - Marked With @classmethod Decorator To Flag It As Class Method
# P# @classmethod
# P# def show_classmethods(cls):
# @@ اجباري وضع Parameters ال cls
# - It Take Cls Keyword to Parameter Not Self To Point To The Class not The Instance
# todo مش محتاج تنشاء Inctance من ال class المستخدم  علشان تشغل ال Methods
# - It Doesn't Require Creation of a Class Instance
# todo ويتم استخدمها عندما تريد التعامل مع ال class مش ال Instance
# - Used When You Want To Do Something With The Class Itself
# >--------------------------------------------------------------------------
# B~ عند استخدام ال Static Methods
# P# نستخدم ال Keyword التالي
# C% @staticmethod
# P# def say_hello():
# Static Methods: => @staticmethod Keyword
# - It Takes No Parameters
# P# لا تحتاج الي Parameters ويمكنك وضع اي عدد Parameters كما تشاء
# - Its Bound To The Class Not Instance
# @@ يتم استخدام نوع ال staticmethod لعمل شي معين يخص ال class بدون عمل access علي ال class ولا ال Object
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------
# class Member:

#   not_allowed_names = ["Hell", "Shit", "Baloot"]

#   users_num = 0
#! يتم عمل ال @classmethod بهذا الشكل وعند عملها بهذا الشكل تكون تخص ال class ليست تخص ال Instance
#   @classmethod
#! وتاخذ class => ( cls ) Parameter مش زي ال Instance => ( self )
#   def show_users_count(cls):

#     print(f"We Have {cls.users_num} Users In Our System.")

#   @staticmethod
#   def say_hello():

#     print("Hello From Static Method")

#   def __init__(self, first_name, middle_name, last_name, gender):

#     self.fname = first_name

#     self.mname = middle_name

#     self.lname = last_name

#     self.gender = gender

#     Member.users_num += 1  # Member.users_num = Member.users_num + 1

#   def full_name(self):

#     if self.fname in Member.not_allowed_names:

#       raise ValueError("Name Not Allowed")

#     else:

#       return f"{self.fname} {self.mname} {self.lname}"

#   def name_with_title(self):

#     if self.gender == "Male":

#       return f"Hello Mr {self.fname}"

#     elif self.gender == "Female":

#       return f"Hello Miss {self.fname}"

#     else:

#       return f"Hello {self.fname}"

#   def get_all_info(self):

#     return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#   def delete_user(self):

#     Member.users_num -= 1  # Member.users_num = Member.users_num -1

#     return f"User {self.fname} Is Deleted."

# print(Member.users_num)

# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)
# print(member_four.delete_user())
# print(Member.users_num)

# Member.show_users_count()

# print(member_one.full_name())
# print(Member.full_name(member_one))

# Member.say_hello()
# ? -------------------------------------- 109 ------------------------------------------------------
# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# @@ كل حاجه في البايثون عباره عن Object
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
# Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------
# class Skill:

#     def __init__(self):

#         self.skills = ["Html", "Css", "Js"]

#     def __str__(self):

#         return f"This is My Skills => {self.skills}"

#     def __len__(self):

#         return len(self.skills)

# print(Skill().__len__())
# profile = Skill()
# print(Skill().skills)
# print(Skill().__str__())
# print(profile)
# print(len(profile))

# profile.skills.append("PHP")
# profile.skills.append("MySQL")

# print(len(profile))

# print(profile.__class__)
# my_string = "Osama"
# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))
# print(dir(len))
# print(str.upper(my_string))
# ? -------------------------------------- 110 ------------------------------------------------------
# ------------------------------------------------
# -- Object Oriented Programming => Inheritance #! الوراثه --
# ------------------------------------------------
# class Food:  # Base Class

#     def __init__(self, name, price):

#         self.name = name

#         self.price = price

#         print(f"{self.name} Is Created From Base Class And Price Is {self.price}")

#     def eat(self):

#         print("Eat Method From Base Class")

#! يمكننا وراثه class بداخل class ثاني من خلال (اسم ال class الذي سوف يتم الوراثه منه)
#! Name_class_2th(Name_class_1th)
# class Apple(Food):  # Derived Class

# def __init__(self, name, price, amount):

# ^^ (بشكل مبتتداء) لعمل وراثه للاشياء الذي بداخل ال Instance ذات نفسها الي هي القيم الذي تم صنعها
# Food.__init__(self, name,price)  # Create Instance From Base Class

# P# (بشكل متقدم)  لعمل وراثه للاشياء الذي بداخل ال Instance ذات نفسها الي هي القيم الذي تم صنعها
#  super().__init__(name,price)

# todo يتم عمل وراثه لل قيم الذي مثل هذه من خلال استخدام ال super()
#      self.amount = amount

#      print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")


#     def get_from_tree(self):

#      print(f"Get From Tree From Derived Class Price => {self.price}")

# food_one = Food("Pizza",17)
# food_two = Apple("Pizza", 150, 500)
# food_two.eat()
# food_two.get_from_tree()
# ? -------------------------------------- 111 ------------------------------------------------------
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------
# class BaseOne:

#     def __init__(self):

#         print("Base One")

#     def func_one(self):

#         print("One")

#     def Override(self):
#         print("You Override From BaseOne")

# class BaseTwo:

#     def __init__(self):

#         print("Base Two")

#     def func_two(self):

#         print("Two")

# B~ عمل Override علي نفس اسم inctance الي قبلها
#     def Override(self):

#         print("You Override From BaseTwo")

# P# عند الوراثه من اكثر من مكان هذا يترتب علي حسب ترتبهم في الخانه

# class Derived(BaseOne, BaseTwo):

#     pass

# my_var = Derived()

# P# لمعرفه ترتيب العناصر
# print(Derived.mro())
# overOne = BaseOne.Override
# overTwo = BaseTwo.Override
# overOne(BaseOne)
# overTwo(BaseOne)
# print(my_var.func_one)
# print(my_var.func_two)

# my_var.func_one()
# my_var.func_two()

# @@ هذه هو ال Multiple Inheritance ان يتم وراثه من من اكثر من شخص عمل الوراثه من شخص اخري بمعني انك ترث خصائص الشخص الاول

# class Base:

#     pass

# class DerivedOne(Base):

#     pass

# class DerivedTwo(DerivedOne):

#     pass
# ? -------------------------------------- 112 ------------------------------------------------------
# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism #? تعداد الاوجه--
# @@ تعدد الاوجه ان يتم وراثه شي معين ويمكنك التحكم به ع حسب المكان الذي تستخدمه به
# -------------------------------------------------
# class A:

#   def do_something(self):

#     print("From Class A")

# ^^ هنا عملنا هذا ال ERROR لكي لا تستخدم نفس ال output وتعدله علي حسب ماتريد
# raise NotImplementedError("Derived Class Must Implement This Method")

# B~ هنا تم عمل OverRide علي نفس اسم inctance من ال A
# class B(A):

#   def do_something(self):

#     print("From Class B")

# class C(A):

#   def do_something(self):

#     print("From Class C")

# my_instance0=A()
# my_instance0.do_something()
# my_instance = B()
# my_instance.do_something()
# my_instance1 = C()
# my_instance1.do_something()
# ? -------------------------------------- 113 ------------------------------------------------------
# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# ? يكون عباره عن استخدام العادي لل class يكون كل شي متاح ويمكننا التعديل علي عناصره
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# ? عباره عن Attributes and Methods يمكنك الدخول عليهم من خلال ال class و ال class الذي يرث الخصائص
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# ? يمكنك الدخول اليها من خلال ال class , Object فقط
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# @@ لايمكن عمل Modified بره ال class
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------
# class Member:

#   def __init__(self, name):
# #^^ وهذا شكل ال Public الطبيعي الذي نعرفه
#     self.name = name  # Public

# one = Member("Ahmed")
# print(one.name)
# one.name = "Sayed"
# print(one.name)

# class Member:

#   def __init__(self, name):
# ^^ هذا يكون شكل ال Attributes ال Protected يكون قبلها _ (_name)
#     self._name = name  # Protected

# one = Member("Ahmed")
# print(one._name)
# one._name = "Sayed"
# print(one._name)

# class Member:

#   def __init__(self, name):
# ^^ هذا يكون شكل ال Attributes ال Private يكون قبلها __ (__name)
#     self.__name = name  # Private

#   def say_hello(self):

#     return f"Hello {self.__name}"

# one = Member("Ahmed")
# print(one.say_hello())
# @@ يمكننا عمل Access علي ال Private بهذا الشكل
# print(one._Member__name)
# ? -------------------------------------- 114 ------------------------------------------------------
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------
# class Member:

#     def __init__(self, name):

#         self.__name = name  # Private

#     def say_hello(self):

#         return f"Hello {self.__name}"

# @@ هذه طريقه الصحيحه لعمل Getter للبيانات ال Private
# def get_name(self):  # Getter

#     return self.__name

# @@ هذه طريقه الصحيحه لعمل Setters للبيانات ال Private ان تعدل عليها
#     def set_name(self, new_name):  # Setters

#         self.__name = new_name

# one = Member("Ahmed")

# todo هذه طريقه غير سليمه للتعامل مع البيانات ال Private
# one._Member__name = "Sayed"
# print(one._Member__name)

# print(one.get_name())
# one.set_name('Abbas')
# print(one.get_name())
# ? -------------------------------------- 115 ------------------------------------------------------
# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------
# class Member:

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

#     def say_hello(self):

#         return f"Hello {self.name}"

# P# عند تحويل ال Object نستخدم @property قبل ال Object بهذا الشكل لكي يمكننا المناده عليها بشكل عادي
# @property
# def age_in_days(self):

# return self.age * 365

# one = Member("Ahmed", 40)

# print(one.name)
# print(one.age)
# print(one.say_hello())
# print(one.age_in_days())

# print(one.age_in_days)
# ? -------------------------------------- 116 ------------------------------------------------------
# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# P# يتسخدم لعمل بنيه لشي معين ولكن لاتنطبق عليه نفسه وتنطبق علي الذي يرثها منه
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------
# @@ نستعدي من ال abc النوعين دول لكي يتم تفعلهم
# from abc import ABCMeta, abstractmethod

#! تستخدم ال ABCMeta بهذا الشكل
# class Programming(metaclass=ABCMeta):

#! تستخدم ال @abstractmethod بهذا الشكل
#   @abstractmethod
#   def has_oop(self):

#     pass

#! عند عمل اكثر من @abstractmethod لازم نعملهم كلهم في باقي ال class الي بيرث الحاجه دي
#   @abstractmethod
#   def has_name(self):

#     pass

# class Python(Programming):

#   def has_oop(self):

#     return "Yes From Python"

#   def has_name(self):

#     return "Printed From Python"

# class Pascal(Programming):

#   def has_oop(self):

#     return "No From Pascal"

#   def has_name(self):

#     return "Printed From Pascal"

# one = Python()
# two = Pascal()

# print(one.has_oop())
# print(one.has_name())
# print(two.has_oop())
# print(two.has_name())
# ? -------------------------------------------------------------------------------------------- EX 116-103
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# class Game:
#     def __init__(self,name,developer,year,price_in_pounds):
#         self.name= name
#         self.developer=developer
#         self.year=year
#         self.price_in_pounds=price_in_pounds

# game_one = Game("Ys", "Falcom", 2010, 780)
# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds:.1f} Egyptian Pounds", end="")

# Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# class User:

#     def __init__(self, name, lname, age, gender):
#         self.name = name
#         self.lname = lname
#         self.age = age
#         self.gender = gender
# >-------------------------
# def gender_title(self):
#     if self.gender == "Male":

#         return f"Hello Mr {self.name} {self.lname:.1s}."
#     elif self.gender == "Female":

#         return f"Hello Mrs {self.name} {self.lname:.1s}."
# def full_details(self):
#     return f"{self.gender_title()} [{str(40-self.age).zfill(2)}] Years To Reach 40"
# >-------------------------
# def full_details(self):
#     if self.gender == "Male":

#         return f"Hello Mr {self.name} {self.lname:.1s}. [{str(40-self.age).zfill(2)}] Years To Reach 40"

#     elif self.gender == "Female":

#         return f"Hello Mrs {self.name} {self.lname:.1s}. [{str(40-self.age).zfill(2)}] Years To Reach 40"

# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40
# >---------------------------------------
# ^^ Assign 3
# >---------------------------------------
# class Message:

#   @classmethod
#   def print_message(cls):
#     return "Hello From Class Message"


# print(Message.print_message())
# >---------------------------------------
# ^^ Assign 4
# >---------------------------------------
# class Games:
#     def __init__(self, namegame):

#         self.namegame = namegame

#     def show_games(self):
#         if self.namegame.__class__ is str:
#             print(f"I Have One Game Called \"{self.namegame}\"")
#         if self.namegame.__class__ is list:
#             print("I Have Many Games:")
#             for x in self.namegame:
#                 print(f"-- {x}")
#         if self.namegame.__class__  is int:
#             print(f"I Have {self.namegame} Game.")

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()
# my_games_names.show_games()
# my_games_count.show_games()
# >---------------------------------------
# ^^ Assign 5
# >---------------------------------------
# class Members:

#     def __init__(self, n, p):

#         self.name = n

#         self.permission = p

#     def show_info(self):
#         if self.permission == "Admin":
#             return f"Your Name Is {self.name} And You Are Admin"
#         else:
#             return f"Your Name Is {self.name} And You Are Moderator"

# class Admins(Members):
#     # def __init__(self, n, p):
#     #     Members.__init__(self, n, p)
#     pass

# class Moderators(Admins):
#     # def __init__(self, n, p):
#     #     super().__init__(n, p)
#     pass

# member_one = Admins("Osama", "Admin")
# member_two = Moderators("Ahmed", "Moderator")
# member_3 = Moderators("Sona", "Moderator")

# print(member_one.show_info())
# print(member_two.show_info())
# print(member_3.show_info())
# >---------------------------------------
# ^^ Assign 6
# >---------------------------------------
# class A:

#   def __init__(self, one):

#     self.one = one

# class B:

#   def __init__(self, two):

#     self.two = two

# class C:

#   def __init__(self, three):

#     self.three = three

# class Text(A,B,C):
#     def __init__(self,one,two,three):
#       A.__init__(self,one)
#       B.__init__(self,two)
#       C.__init__(self,three)
#     def show_name(self):
#         return f"The Name Is => {self.one}{self.two}{self.three}"

# the_name = Text("El", "ze", "ro")

# print(the_name.show_name())
# ? -------------------------------------- 117 ------------------------------------------------------
# ------------------------
# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------
# ? -------------------------------------- 118 ------------------------------------------------------
# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------
# @@ نستدعي ال SQLite من خلال ال import sqlite3
# Import SQLite Module
# import sqlite3

# @@ يتم انشاء ال DB من خلال sqlite3.connect("Name File")
# Create Database And Connect
# db = sqlite3.connect("app.db")

# @@ لعمل ال DB نستخدم اسم ال متغير الذي تم عمله ثم نستخدم كلمه execute
# Create The Tables and Fields
# B~ وعند كتابه البيانات نكتب create table is not exists ثم اسم ملف البيانات
# B~ وبداخل ال (البيانات ذات نفسها)
# db.execute(
# "create table if not exists skills (name text, progress integer, user_id integer)")

# J$ لغلق الملف بعد الانتهاء
# Close Database
# db.close()
# ? -------------------------------------- 119 ------------------------------------------------------
# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------
# import sqlite3

# db = sqlite3.connect("app.db")

# ^^ نستخدم ال cursor لوضع مؤسر الماوي في مكان معين وهذه هو الاعتماد الكلي للاستخدام
# cr = db.cursor()

# Create The Tables and Fields
# cr.execute("create table if not exists users (user_id integer , name text)")
# cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# P# هذا شكل يدائي لعمل البيانات طبعا يمكننا عمل LooP بشكل عادي كما سوف نفعل
# ^^ Inserting Data نضع البيانات بداخل ال DB بهذا الشكل
# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')")

# my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]

# ? ونعمل loop طبيعي بهذا الشكل طبعا
# for key,value in enumerate(my_list,1):
#   cr.execute(f"insert into users(user_id, name) values({key}, '{value}')")

#! نستخدم ال commit لحفظ البيانات الذي تم وضعها وهذه اهم خطوه لتنفيذ ما تم عمله
# db.commit()

# db.close()
# ? -------------------------------------- 120 ------------------------------------------------------
# import sqlite3

# db = sqlite3.connect("app.db")

# cr = db.cursor()

# cr.execute("create table if not exists users (user_id integer , name text)")
# cr.execute(
#     "create table if not exists skills (name text, progress integer, user_id integer)")

# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')")

# @@ لاستدعاء بينات معينه من داخل ال users الي هي الاسماء وهذه تستخدم لجلب حقل واحد
# cr.execute("select name from users")

# @@ لاستدعاء بينات معينه من داخل ال users الي هي الاسماء وهذه تستخدم لجلب حقلين من البيانات
# cr.execute("select user_id,name from users")

# @@ لاستدعاء بينات معينه من داخل ال users الي هي الاسماء وهذه تستخدم لجلب جميع الحقول باستخدام ال *
# cr.execute("select * from users")

# @@ عند استخدام fetchone بيجبلك اول عنصر او عنصر واحد فقط الي هو اول واحد ولجلب جميع العناصر يمكنك تكرار الكود كذا مره
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# @@ عند استخدام fetchall يجلب لك كل العناصر علي هياء LIst بداخلها Tuple
# print(cr.fetchall())

# @@ عند استخدام fetchmany يجلب لك كل العناصر علي هياء LIst بداخلها Tuple ولكن هنا يحتاج منك عدد العناصر الذي تريدها
# print(cr.fetchmany(2))

# db.commit()

# db.close()
# ? -------------------------------------- 121 ------------------------------------------------------
# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------
# import sqlite3
# # Function to Get DataBase my App
# def get_all_data():
#     try:

#         # Connect To Database
#         db = sqlite3.connect("app.db")

#         # Print Success Message
#         print("Connected To Database Successfully")

#         # Setting Up The Cursor
#         cr = db.cursor()

#         # Fetch Data From Database
#         cr.execute("select * from users")

#         # Assign Data To Variable
#         results = cr.fetchall()

#         # Print Number Of Rows
#         print(f"DataBase Has {len(results)} Rows.")

#         # Printed Message
#         print("Showing Data: ")

#         # Loop On Result
#         for key, row in results:
#             print(f"UserID => {key}, Username => {row}")

# for row in results:
#   print(f"UserID => {row[0]},", end=" ")
#   print(f"Username => {row[1]}")

# تم استخدم هنا كلمه as لعمل اختصار لاسم sqlite3.Error وتم تغيره الي SE
#     except sqlite3.Error as SE:

#         print(f"Error Reading Data {SE}")

#     finally:

#         if(db):

#             db.close()

#             print("Connection To Database Is Closed")


# get_all_data()
# ? -------------------------------------- 122 ------------------------------------------------------
# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------
# Import SQLite Module
# import sqlite3

# Create Database And Connect
# db = sqlite3.connect("app.db")

# Setting Up The Cursor
# cr = db.cursor()

# Update Data
# ^^ لعمل تحديث للبيانات من شي الي اخري
# ^^ update users set اسم ال table = ثم القيمه الجديده لل لعنصر الاول او علي حسب العنصر الذي تريد تحديثه
# ^^ ونستخدم كلمه where ثم اسم ال user_id ونضع بجانبه رقمه لكي تغير شخص او علي حسب طلبك
# cr.execute("update users set name = 'Mahmoud' where user_id = 1")
# cr.execute("update users set name = 'Sayed' where user_id = 2")
# cr.execute("update users set name = 'Ameer' where user_id = 3")

# Delete Data
# ^^ لحذف قيمه معينه من خلال ال user_id بيتم كتابتها بهذا الشكل
# cr.execute("delete from users where user_id = 4")

# ^^ لحذف كل العناصر
# cr.execute("delete from users")

# Fetch Data
# cr.execute("select * from users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# Save (Commit) Changes
# db.commit()

# Close Database
# db.close()
# ? -------------------------------------- 123_124_125_126 ---------------------------------------------------
# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 1 --
# -----------------------------------------------------
# import sqlite3  # Import SQLite Module

# db = sqlite3.connect("app.db")  # Create Database And Connect

# cr = db.cursor()  # Setting Up The Cursor

# def commit_colde():  # Commit And Close Method
#     """Commit Changes and Close Connection To Database"""
#     db.commit()  # Save (Commit) Changes
#     db.close()  # Close Database
#     print("Connection To Database Is Closed")

# uid = 5  # My User ID

# # Input Big Message
# input_message = """
# What Do You Want To Do ?
# "s" => Show All Skills
# "a" => Add New Skill
# "d" => Delete A Skill
# "u" => Update Skill Progress
# "q" => Quit The App
# Choose Option : """

# user_input = input(input_message).strip().lower()  # Input Option Choose

# commands_list = ["s", "a", "d", "u", "q"]  # Command List

# def show_skills():  # Define The Methods

#     cr.execute(f"select * from skills where user_id ='{uid}'")

#     results = cr.fetchall()

#     print(f"You Have {len(results)} Skills.")

#     if len(results) > 0:

#         print("Showing Skills With Progress: ")

#     for row in results:

#         print(f"Skills => {row[0]},", end=" ")

#         print(f"Progress => {row[1]}%")

#     commit_colde()

# def add_skill():

#     sn = input("WRite Skill Name: ").strip().capitalize()

#     cr.execute(
#         f"select name from skills where name ='{sn}' and user_id ='{uid}'")

#     results = cr.fetchone()

#     if results == None:
#         prog = input("WRite SKill Progress: ").strip()

#         cr.execute(
#             f"insert into skills(name,progress,user_id) values('{sn}','{prog}','{uid}')")  # Theres No Skill With This Name In Database

#         print(f"Your Skill Name => {sn} and Progress => {prog}")

#     else:# Theres A Skill With This Name in Database
#         print("You Can't Add This Skill Beacuse This SKill in DB.")

#         option = input(
#             "if Need To Update You Progress WRite (y) Or (n) To Close: ")

#         if option == "y":
#              new_prog = input("WRite The New Skill Progress: ").strip()

#              cr.execute(f"update skills set progress ='{new_prog}' where name ='{sn}' and user_id ='{uid}'")

#              print(f"Your Skill Name => {sn} and New Progress => {new_prog}%")

#     commit_colde()

# def delete_skill():

#     sn = input("WRite Skill Name: ").strip().capitalize()

#     cr.execute(
#         f"delete from skills where name ='{sn}' and user_id ='{uid}'")

#     print(f"Your Skill Name => {sn} In ID ({uid}) Has Deleted.")

#     commit_colde()

# def update_skill():

#     sn = input("WRite Skill Name: ").strip().capitalize()

#     new_prog = input("WRite The New SKill Progress: ").strip()

#     cr.execute(
#         f"update skills set progress ='{new_prog}' where name ='{sn}' and user_id ='{uid}'")

#     print(f"Your Skill Name => {sn} and New Progress => {new_prog}")

#     commit_colde()

# if user_input in commands_list:  # Check If Command Is Exists

#     if user_input == "s":

#         show_skills()

#     elif user_input == "a":

#         add_skill()

#     elif user_input == "d":

#         delete_skill()

#     elif user_input == "u":

#         update_skill()

#     else:

#         print("App Is Closed.")
#         commit_colde()

# else:

#     print(f"Sorry This Command \"{user_input}\" Is Not Found")
# ? -------------------------------------- 127 ------------------------------------------------------
# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------
# Import SQLite Module
# import sqlite3

# Create Database And Connect
# db = sqlite3.connect("app.db")

# Setting Up The Cursor
# cr = db.cursor()

# my_tuple = ('Pascal', '65', 4)

# Inserting Data
# P#                                                                           بعض اوامر ال ((SQL)) الذي سوف تفيدنا في الحياه العمليه
# cr.execute("insert into skills values('Pascal', '65', 4)")
#! لمنع ال SQL Injection نستخدم هذا الشكل من وضع البيانات
# نضع مكان ال values ثلاث علامات استفهام (?,?,?) ثم ال values الذي تريد وضعها
# cr.execute("insert into skills values(?, ?, ?)",('Asoum', '65', 4))
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)

# Fetch Data From Database
# @@ نستخدم كلمه order by لترتيب العناصر علي حسب ماتريد ونستخدم وللترتيب التصادعي نستخدم asc
# cr.execute("select * from skills order by user_id asc")
# @@ وللترتيب التصادعي نستخدم desc
# cr.execute("select * from skills order by user_id desc")
# @@ وللترتيب العكسي نستخدم desc
# cr.execute("select * from skills order by name desc")
# @@ لتحديد العناصر الذي تريد ان تظهر لك نستخدم كلمه limit ثم العدد
# cr.execute("select * from skills order by name limit 2")
# @@ نستخدم offset ثم الرقم الذي تريد ان يبداء بعده
# cr.execute("select * from skills order by name limit 4 offset 2")
# @@ ان يبداء طباعه الارقام الذي اكبر او اصغر من الذي تريد وضعه
# cr.execute("select * from skills where user_id >= 2")

# @@ يمكننا استخدم ال no in ++ ,و ال in هنا بشكل عادي جدا ايضا
# ? هنا تقول له اذا كان ال id بداخل ال tuple الي قدامك دي اطبعهم (in -,-,-)
# cr.execute("select * from skills where user_id in(1, 4)")
# ? هنا تقول له اذا كان ال id ليس بداخل ال tuple الي قدامك دي اطبعهم (not in -,-,-)
# cr.execute("select * from skills where user_id not in(1, 2, 3)")

# Assign Data To Variable
# results = cr.fetchall()

# Loop On Results
# for row in results:
# print(f"Skill Name => {row[0]},", end=" ")
# print(f"Skill Progress => {row[1]},", end=" ")
# print(f"User ID => {row[2]}")

# Save (Commit) Changes
# db.commit()

# Close Database
# db.close()
# ? -------------------------------------------------------------------------------------------- EX 127-117
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# MongoDB
# MySQL
# SQLite
# SQL Server
# Oracle
# >---------------------------------------
# ^^ Assign 2_3_4_5
# >---------------------------------------
# import sqlite3
# db = sqlite3.connect("eldeep.db")
# cr = db.cursor()
# cr.execute(
#     "create table if not exists users (user_id integer unique,name text unique, dob text unique, Email text unique)")
# my_num = [1, 2, 3, 4, 5]
# my_names = ["Ahmed", "Sayed", "Gamal", "Mahmoud", "Sameh"]
# my_dob = ["06/22/2000", "07/29/2000", "01/20/1999", "09/20/2000", "01/11/2000"]
# my_mail = ["a@elzero.org", "w@elzero.org",
#            "q@elzero.org", "m@elzero.org", "s@elzero.org"]

# for i in range(len(my_num)):
#     globals
#     try:
#         cr.execute(
#             f"insert into users values({my_num[i]}, '{my_names[i]}','{my_dob[i]}','{my_mail[i]}')")
#     except:
#         print("The Data Already Exists")

# cr.execute("select * from users")

# results = cr.fetchall()

# print(results[4])

# type_id=int(input("WRite Your ID : ").strip())
# cr.execute(f"select * from users where user_id ={type_id}")
# results = cr.fetchone()
# if results == None:
#     print("User Not Found.")
# else:
#     cr.execute(f"delete from users where user_id ={type_id}")
#     print("User Deleted.")
#     print("Show Other Data:")
#     cr.execute("select * from users")
#     resulte=cr.fetchall()
#     for row in resulte:
#         print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")

# db.commit()
# db.close()
# ? -------------------------------------- 128 ------------------------------------------------------
# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# ! هنا عند استخدام ال __name__ بداخل الملف الاساسي يعني انه هو ال __main__
# ! لو تم استدعاء الملف من خلال ال import هنا لم يكن نوعه __main__ لانه تم استدعاء
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------
# print(__name__)
# ? -------------------------------------- 129 ------------------------------------------------------
# ------------------------------------------------------
# P# يتم استخدام هذا الشكل بشكل Advanced لقياس الوقت الذي تم انهاء في الكود الخاص بك
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# ^^ stmt = الكود الذي تريد ان تحسب الوقت بتاعه
# - stmt: Code You Want To Measure The Execution Time
# ^^ setup = عمل شي معين مثال import Module او اشي شي علي حسب الفكره
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# ^^ timer = وقت الشي الذي سوف يحدث
# - timer: The Timer Value
# ^^ number = عدد الشي الذي سوف يتم تنفيذه
# - number: How Many Execution That Will Run
# -------------------------------------------------------
# import timeit

# print(dir(timeit))
# P# عند عمل العمليه سوف يطبع لك اقل وقت تم عمل في ال 1.000.000 عمليه بمعني ان لو في عمليه تم عملها ف نص ثانيه وهي اقل وقت تم عملها ف ال 1.000.000 سوف يتم طباعتها
# print(timeit.timeit("'Elzero' * 1000")) # => 0.6548549000001458

# name = "Elzero"

# print(name * 1000)

# print(timeit.timeit("name = 'Elzero'; name * 1000"))

# print(random.randint(0, 50))

# ^^ عند وضع بداخل ال stmt شي يجب استدعاء ف ال stup من خلال هويته
# print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
# ^^ عند استخدام ال repeat تحدد له عدد مرات اعاده العمليه * 1.000.000 مره
# print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
# ? -------------------------------------- 130 ------------------------------------------------------
#! (explorer .) نستخدمها لفتح الملف الذي نحن به في ال command Line
# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# ^^ انواع ال ERROR الذي يمكنك ان تتبعها
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# P# filename = اسم الملف بالاكستينشن بتاعه.log >>> my_logging.log
# - filename => File Name and Extension
# P# filemode = نوع ال mode بتاع الملف اذا كان ('a',,'r',,'w') الافضل بتكون استخدام ال 'a' لان بيتم كتابه الرساله بعد الرساله القديمه وهكذا علي حسب الفكره
# - filemode => Mode Of The File a => Append
# P# format = الرساله الذي تريد ان تظهر لك
# - format => Format For The Log Message
# P# levelname = اسم ال ERROR المستخدم
# - levelname => Level of Severity
# P# datefmt = نوع كتابه ال Data وهذا من خلال درس الوقت الذي اخدنا
# - datefmt => Type Date
# ------------------------
# ^^ تستخدم لاسترجاع لك اسم ال logger الي هو ال RooT ويمكننا تغيره بشكل عادي جدا
# getLogger => Return a Logger With the Specified Name
# ------------------------
# P# %(asctime)s => ليطبع كل الوقت الذي حدث به ال ERROR وطبعا يتم استخدامها بهذا الشكل  %(..)s
# P# %(name)s => اسم ال RooT وعلي حسب ما تريد تغيره
# P# %(levelname)s => اسم ال ERROR المستخدم
# P# %(message)s => الرساله الذي بداخل ال ERROR
# P# %(filename)s => اسم الملف الذي نحن بها -- Prog.py
# ? ------------------------
# import logging

# print(dir(logging))

# logging.basicConfig(filename="my_logging.log",
#                     filemode="a",
#                     format="(%(asctime)s) | %(name)s | %(levelname)s => $%(message)s# And File Name => %(filename)s",
#                     datefmt="%d %B %Y, %H:%M:%S")

# my_logger = logging.getLogger("Anonymous Deep") #B~ لتغير اسم ال Root الي الذي تريده بشكل عادي

# logging.error("This Is ERROR Message")
# my_logger.critical("This Is Critical Message")
# ? -------------------------------------- 131 ------------------------------------------------------
# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# P# اختبار وحدات الكود بتاعك من خلال ال unittest
# ^^ هو نوع معين من البيانات الذي انتظره يمعني ان يتم عمل test لكل الاكواد الذي لدينا وننتظر قيمه معينه
# ----------------------------------------------------
# Test Runner
# C% انواع Module الذي تستخدم لعمل ال Test هي => (unittest, pytest)
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# @@ اقل وحدات في ال test هي test Case
# - Smallest Unit Of Testing
# @@ نستخدم Methods ال Asserts لمعرفه الشي الذي سوف يسترجع من خلال ال test Case
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suitea
# @@ ال Test Suitea هي مجموعه من ال Test Cases مع بعض بمعني انه كذا مجموعه من ال Test Cases
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# @@ ال Test Report هي نتيجه ال Test الذي حدث
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------
# import unittest
# @@ نستخدم ال assert ثم الكود الذي تريد التجريه عليه والبيانات الذي تنتظرها منه ثم رساله اذا لم تطلع النتيجه صحيحه
# assert الكود == الاخراج, "الرساله"0
# assert 3 * 8 == 24, "Should Be 24"

# @@ هذا يكون شكل عمل ال test case مانول
# def test_case_one():

#   assert 5 * 10 == 50, "Should Be 50"

# def test_case_two():

#   assert 5 * 50 == 250, "Should Be 250"

# if __name__ == "__main__":

#   test_case_one()
#   test_case_two()

#   print("All Tests Passed")
# >---------------------------------------
# هذا class مخصوص لل unittest ويتم استخدام بداخله (unittest.TestCase)
# class MyTestCase(unittest.TestCase):

#     def test_one(self):
# # وعلي حسب ما الفكره الذي لديك تضتع ال Assert...
#         self.assertTrue(100 > 99, "Should Be True")

#     def test_two(self):

#         self.assertEqual(40 + 60, 100, "Should Be 100")

#     def test_three(self):

#         self.assertGreater(100, 90, "Should Be True")

#     def test_Four(self):

#         self.assertFalse(5 != 5, "Should Be False")


# if __name__ == "__main__":

#     unittest.main()
# ? -------------------------------------- 132 ------------------------------------------------------
# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# ^^ فكره عمل ال Serial Numbers بشكل عشوائي
# --------------------------------------------------------
# نستخدم import لل string بداخلها الحروف الكبيره والصغيره وجميع الارقام
# import string
# import random

# print(string.digits) => 0123456789
# print(string.ascii_letters) => abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase) => abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase) => ABCDEFGHIJKLMNOPQRSTUVWXYZ

# def make_serial(count):

#     all_chars = string.ascii_letters + string.digits

#     chars_count = len(all_chars)

#     serial_list = []

#     while count > 0:

#         random_number = random.randint(0, chars_count - 1)

#         random_character = all_chars[random_number]

#         serial_list.append(random_character)

#         count -= 1  # count = count - 1

#     print("".join(serial_list))

# make_serial(30)
# ? -------------------------------------------------------------------------------------------- EX 133-128
# >---------------------------------------
# ^^ Assign 1
# >---------------------------------------
# import unittest

# class unittest_Module(unittest.TestCase):
#     def test_one(self):
#         liss = [5, 7, 8, 10]
#         self.assertIn(10, liss, "10 Not Found In List")
#         print("Access 10 Found in Your List")
#     def test_two(self):
#         self.assertIs(type(10),int,"Your Expr Not Int")
#         print("Your Input is Int ALready")
#     def test_th(self):
#         self.assertTrue(100,"Your Input Not True")
#         print("Number 100 ALready True")
#     def test_four(self):
#         self.assertTrue([],"False")
#         print("You WRite False Value")
#     def test_five(self):
#         self.assertTrue(100>=90,"False Value")
#         print("100 is Lager 90 ALready")

# if __name__ == "__main__":

#     unittest.main()
# >---------------------------------------
# ^^ Assign 2
# >---------------------------------------
# import string
# import random

# def make_serial(count):
#     all_chars = string.ascii_lowercase+string.digits
#     chars_count = len(all_chars)
#     serial_list = []

#     while count > 0:

#         random_number = random.randint(0, chars_count - 1)

#         random_character = all_chars[random_number]

#         serial_list.append(random_character)

#         count -= 1  # count = count - 1

#         if len(serial_list) == 4:
#             print("".join(serial_list)+"-", end="")
#         if len(serial_list) == 4:
#             print("".join(serial_list)+"-", end="")
#         elif len(serial_list) == 6:
#             print("".join(serial_list))

# make_serial(14)
# C%                                                                     End Course In 4/9/2022
