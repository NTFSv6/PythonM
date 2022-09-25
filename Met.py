
# @@ type(البيانات الذي تريد معرفه نوعها)   تستخدم لمعرفه نوع البيانات

# print(type("OMAr"))  # => String جمله او كلمه معينه مكتوبه تسمي
# print(type(1545))  # => Integer الرقم يسمي
# print(type(1.2))  # => float الرقم العشري يسمي
# print(type({1}))  # => set نوع البينات هنا
# print(type([1, 2]))  # => list نوع البيانات هنا
# print(type((1, 1)))  # => tuple نوع البيانات هنا
# print(type({"ONE": 1, "TWO": 2, "three": 3}))  # => Dictionary
# # => dict تستخدم لكتابه كلمه ومعنها
# print(type(2 == 2))  # => Boolean  -- true _ false

# >----------------------------------------------------- -----------------------------------------------------
# >----------------------------------------------------- -----------------------------------------------------
# B~ \b => Back Space تعمل حذف لاخر حرف
# B~ \newline => Escape New Line + \ تستخدم لكتابه الكلام في سطر واحد اذا كانو منفصلين
# B~ \\ => Escape Back Slash لطباعه ال back slash نستخدم 2 منها
# B~ \' => Escape Single Quotes لطباعه ال Single Slash
# B~ \" => Escape Double Quotes لطباعه ال Double Slash
# B~ \n => Line Feed لعمل سطر جديد
# B~ \r => Carriage Return يحذف عدد الحروف او الارقام الذب يعد استخدمها
# B~ \t => Horizontal Tab لعمل tab بين الكلام
# B~ \xhh => Character Hex Value تستخدم لكتابه الحروف بشكل ال Hex

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

# >----------------------------------------------------- -----------------------------------------------------
# >----------------------------------------------------- -----------------------------------------------------
#! -- Concatenation -- دمج الاسترينج مع بعض بستخدام ال +

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
# >----------------------------------------------------- -----------------------------------------------------
# >----------------------------------------------------- -----------------------------------------------------
# -- Strings Methods --

# B~ len(a) تستخدم لمعرفه عدد العناصر الموجود عدد الحروف او الارقام
# B~ strip() تستخدم لازاله المسافات من كل الجوانب
# B~ rstrip() تستخدم لازاله المسافات من اللمين
# B~ lstrip() تستخدم لازاله المسافات من الشمال
# B~ title() يجعل اول حرف ف كل كلمه كابتل واي حرف قبله رقم يحوله كابتل ايضا
# B~ capitalize() # ? خاصية capitalize() تقوم بتحويل أول حرف Capital من ال String واذا كان ال String يحتوي على جملة فيها الكثير من الكلمات فانه يقوم بتحويل اول حرف Capital من أول كلمة فقط وباقي الكلمات كل حروفها تكون Small Letter
# B~ zfill() يضيف عدد اصفار معينه علي حسب كام انت وضعت بداخل الاقواس وهذا يكون الافضل
# B~ upper() يجعل الحروف كلها كابتل
# B~ lower() يجعل الحروف كلها صغيره

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

# _ title()
# b = "I Love 2d Graphics and 3g Technology and python"
# print(b.title())

# _ capitalize()
# b = "I Love d Graphics and 3g Technology and python"
# print(b.capitalize())

# _ zfill()
# c, d, e, f = "1", "11", "111", "1111"
# print(c)
# print(d)
# print(e)
# print(f)
# print(c.zfill(4))
# print(d.zfill(4))
# print(e.zfill(4))
# print(f.zfill(4))

# _ upper() يجعل الحروف كلها كابتل
# g = "eldeep"
# print(g.upper())

# _ lower()
# h = "ELDEEP"
# print(h.lower())
# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# -- Strings Methods --

# B~  split() + rsplit() تستخدم لتقطيع المسطره الذي تكون بين الكلام وعند تحديد الشي الذي تريد تقطيعه ايضا
# B~  center(العدد ,"") تستخدم لاضافه حروف قبل وبعد المتغير الذي سوف تستخدمه ويتم العد من بعد عدد الحروف الذي لديك
# B~  count("string",Start,End) تستخدم للبحث عن عدد وجود الحرف او الكلمه الذي سوف تستخدمها
# B~  swapcase() تجعل الحرف بدل ما يكون صغير تجعله كبير والعكس
# B~ startswith() تستخدم لمعرفه المتغير يبداء بشي معين الذي سوف تضعه ام لا
# B~ endswith() تستخدم لمعرفه المتغير ينتهي بشي معين الذي سوف تضعه ام لا

# a = "I Love Python and PHP and MySQL"
# print(a.split())

# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))  # عند وضع شي معين موجود بداخل الاسترنج سوف يحذفه

# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3))  # تستخدم لتقطيع 3 عناصر فقط والباقي سوف يظهر بشكل طبيعي

# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3))  # ? يعمل تقطيع من الشمال

# _ center()
# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @

# _ count()
# f = "I Love Python and PHP Because PHP PHP is Easy"
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 34))  # ? تستخدم للبحث من اول كذا الي كذا

# _ swapcase()
# g = "I Love Python"
# h = "i lOVE pYTHON"
# print(g.swapcase())
# print(h.swapcase())

# _ startswith()
# i = "I Love Python JavaScript"
# print(i.startswith("I"))
# print(i.startswith("J", 14))
# print(i.startswith("P", 7, 12))  # ويمكننا وضع بدايه ونهايه

# _ endswith()
# j = "I Love Python JS"
# print(j.endswith("S"))
# print(j.endswith("n", 7, 13))
# print(j.endswith("e", 2, 6))

# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# -- Strings Methods --

# B~ index(SubString, Start, End) تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
# B~ find(SubString, Start, End)  تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
# B~ rjust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها اللمين
# B~ ljust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها الشمال
# B~ splitlines() تستخدم لكي تسترجع لك list اذا كانت العناصر ليست علي سطر واحد
# B~ expandtabs() تجعلك تتحكم في عدد ال TAB
# B~ istitle() تستخدم لمعرفه هل اول حرف فقط في كل جمله يبداء بحرف كبير ام لا
# B~ isspace() تستخدم لمعرفه هل الشي المستخدم Space ام لا مسطره
# B~ islower() تستخدم لمعرفه هل جميع الحروف صغيره ام لا
# B~ isupper() تستخدم لمعرفه هل جميع الحروف كبيره
# B~ isidentifier() لمعرفه هل هذا الاسم يمكن استخدمه لعمل متغير ام لا
# B~ isalpha() تستخدم لمعرفه هل الحروف الموجوده من (a-z,A-Z)
# B~ isalnum() تستخدم لكي تعرف هل كل الموجود ارقام وحروف
# B~ isnumeric() (0-9) تستخدم لمعرفه هل المتغر او الشي المستخدم ارقام

# _ index()
# a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
#! print(a.index("P", 0, 5))  # Through Error اذا لم يجد الشي الذي تبحث عنه سوف يعمل Error

# _ find()
# b = "I Love Python"
# print(b.find("o"))  # Index Number 3
# print(b.find("P", 0, 10))  # Index Number 7
# print(b.find("P", 0, 5))  # -1 اذا لم يجد الذي تبحث عنه سوف يطبع لك

# _ rjust()
# _ ljust()
# c = "Osama"
# print(c.rjust(10))
# print(c.rjust(10, "#"))
# d = "Osama"
# print(d.ljust(10))
# print(d.ljust(10, "#"))

# _ splitlines()
# e = """First Line
# Second Line
# Third Line"""
# print(e.splitlines())

# _ expandtabs()
# g = "Hello\tWorld\tI\tLove\tPython"
# print(g.expandtabs(10))

# _ istitle()
# a = "Hell And WELCOME Snao My Wndy"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# _ isspace()
# txt = "    "
# print(txt.isspace())

# _ islower()
# five = 'i love python'
# six = 'I Love Python'
# print(five.islower())
# print(six.islower())

# _ isupper()
# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"
# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# _ isidentifier()
# seven = "osama_elzero"
# eight = "OsamaElzero100"
# nine = "Osama@Elzero100"
# print(seven.isidentifier())
# print(eight.isidentifier())
# print(nine.isidentifier())

# _ isalpha()
# x = "AaaaaBbbbbb"
# y = "AaaaaBbbbbb111"
# print(x.isalpha())
# print(y.isalpha()

# _ isalnum()
# u = "AaaaaBbbbbb"
# z = "AaaaaBbbbbb111#"
# print(u.isalnum())
# print(z.isalnum())

# _ isnumeric()
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

# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# -- Strings Methods --

# B~ replace(Old Value, New Value, Count) تستخدم لتبديل شي معين بشي اخر وعلي حسب كام مره تحتاج ان تبدله
# B~ join(Iterable) تستخدم لادخال شي معين داخل ال string

# _ replace()
# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))
# print(a.replace("One", "1", 1))
# print(a.replace("One", "1", 2))

# _ join(Iterable)
# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList))
# print(" & ".join(myList))
# print(", ".join(myList))
# print(type(", ".join(myList)))
# ttt = "KANO"
# print("-".join(ttt)) output => K-A-N-O
# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# -- Lists Methods --

# B~ append() تستخدم لاضافه عنصر جديد الي ال list ولكن يتم اضافته ف الاخر
# B~ extend() تستخدم لادخال كذا list مع بعض بشكل طبيعي
# todo remove() تستخدم لحذف عنصر معين بداخل ال list ولكن اذا كان العنصر متكرر سوف تحذف اول عنصر فقط
# B~ sort() تستخدم لترتيب الارقام والحروف بترتيب الابجدي والحروف من الصغير للكبير وترتب نوع واحد من البيانات لبس كذا نوع
# B~ reverse() تستخدم لعكس مكان العناصر بدل ما هو في الشمال يروح يمين وهكذا

# _ append()
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

# _ extend()
# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["One", "Two"]
# a.extend(b)
# a.extend(c)
# print(a)

# _ remove()
# x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
# x.remove("Osama")
# print(x)

# _ sort()
# ? sort(reverse=True) تستخدم لعكس الترتيب
# y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "B"]
# y.sort(reverse=True)
# print(y)

# _ reverse()
# z = [10, 1, 9, 80, 100, "Osama", 100]
# z.reverse()
# print(z)
# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------

# -- Lists Methods --
# B~ clear() تستخدم لحذف جميع عناصر ال list
# B~ copy() تستخدم لعمل نسخ من list الي list اخري
# B~ count() تستخدم لعد عنصر معين موجود كام مره
# B~ index() تستخدم للبحث عن رقم الانديكس بتاع العنصر الذب سوف تعطيه له يبحث في اول انديكس
# B~ insert() تستخدم لوضع عنصر معين قبل الانديكس الذي سوف تضعه
# B~ pop() تستخدم لوضع الانديكس ويرجع لك بقيمه هذا الانديكس

# _ clear()
# a = [1, 2, 3, 4]
# a.clear()
# print(a)

# _ copy()
# b = [1, 2, 3, 4]
# c = b.copy()
# print(b)  # Main List
# print(c)  # Copied List
# b.append(5)  #? عند اضافه عنصر اخر لا يظهر في ال copy
# print(b)  # Main List
# print(c)  # Copied List

# _count()
# d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
# print(d.count(1))

# _ index()

# e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
# print(e.index("Ahmed"))

# _  insert()
# f = [1, 2, 3, 4, 5, "A", "B"]
# f.insert(0, "Test")
# f.insert(-1, "Test")
# print(f)

# _ pop()
# g = [1, "Omar", 3, 4, 5, "A", "B"]
# print(g.pop(4))
# print(len(g)*g.pop(4))
# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# ! Comment
# ? Comment
# > Comment
# todo Comment
# _ Comment
# @@ Comment مهم
# ^^ Comment
# C% Comment
# T^ Comment
# P# Comment
# V_ Comment
# J$ Comment
# B~ Comment
# >----------------------------------------------------------------------------------------------------------
# >----------------------------------------------------------------------------------------------------------
# B~ len(a) تستخدم لمعرفه عدد العناصر الموجود عدد الحروف او الارقام

# B~ strip() تستخدم لازاله المسافات من كل الجوانب

# B~ rstrip() تستخدم لازاله المسافات من اللمين

# B~ lstrip() تستخدم لازاله المسافات من الشمال

# B~ title() يجعل اول حرف ف كل كلمه كابتل واي حرف قبله رقم يحوله كابتل ايضا

# B~ capitalize() # ? خاصية capitalize() تقوم بتحويل أول حرف Capital من ال String واذا كان ال String يحتوي على جملة فيها الكثير من الكلمات فانه يقوم بتحويل اول حرف Capital من أول كلمة فقط وباقي الكلمات كل حروفها تكون Small Letter

# B~ zfill() يضيف عدد اصفار معينه علي حسب كام انت وضعت بداخل الاقواس وهذا يكون الافضل

# B~ upper() يجعل الحروف كلها كابتل

# B~ lower() يجعل الحروف كلها صغيره

# B~ split() + rsplit() تستخدم لتقطيع المسطره الذي تكون بين الكلام وعند تحديد الشي الذي تريد تقطيعه ايضا

# B~ center(العدد ,"") تستخدم لاضافه حروف قبل وبعد المتغير الذي سوف تستخدمه ويتم العد من بعد عدد الحروف الذي لديك

# B~ count("string",Start,End) تستخدم للبحث عن عدد وجود الحرف او الكلمه الذي سوف تستخدمها

# B~ swapcase() تجعل الحرف بدل ما يكون صغير تجعله كبير والعكس

# B~ startswith() تستخدم لمعرفه المتغير يبداء بشي معين الذي سوف تضعه ام لا

# B~ endswith() تستخدم لمعرفه المتغير ينتهي بشي معين الذي سوف تضعه ام لا

# B~ index(SubString, Start, End) تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه

# B~ find(SubString, Start, End)  تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه

# B~ rjust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها اللمين

# B~ ljust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها الشمال

# B~ splitlines() تستخدم لكي تسترجع لك list اذا كانت العناصر ليست علي سطر واحد

# B~ expandtabs() تجعلك تتحكم في عدد ال TAB

# B~ istitle() تستخدم لمعرفه هل اول حرف فقط في كل جمله يبداء بحرف كبير ام لا

# B~ isspace() تستخدم لمعرفه هل الشي المستخدم Space ام لا مسطره

# B~ islower() تستخدم لمعرفه هل جميع الحروف صغيره ام لا

# B~ isupper() تستخدم لمعرفه هل جميع الحروف كبيره

# B~ isidentifier() لمعرفه هل هذا الاسم يمكن استخدمه لعمل متغير ام لا

# B~ isalpha() تستخدم لمعرفه هل الحروف الموجوده من (a-z,A-Z)

# B~ isalnum() تستخدم لكي تعرف هل كل الموجود ارقام وحروف

# B~ isnumeric() (0-9) تستخدم لمعرفه هل المتغر او الشي المستخدم ارقام

# B~ replace(Old Value, New Value, Count) تستخدم لتبديل شي معين بشي اخر وعلي حسب كام مره تحتاج ان تبدله

# B~ join(Iterable) تستخدم لادخال شي معين داخل ال string

# B~ append() تستخدم لاضافه عنصر جديد الي ال list ولكن يتم اضافته ف الاخر

# B~ extend() تستخدم لادخال كذا list مع بعض بشكل طبيعي

# B~ remove() تستخدم لحذف عنصر معين بداخل ال list ولكن اذا كان العنصر متكرر سوف تحذف اول عنصر فقط

# B~ sort() تستخدم لترتيب الارقام والحروف بترتيب الابجدي والحروف من الصغير للكبير وترتب نوع واحد من البيانات لبس كذا نوع

# B~ sort(reverse=True) تستخدم لترتيب الارقام والحروف بعكس الترتيب الابجدي وعكس جميع البيانات

# B~ reverse() تستخدم لعكس مكان العناصر بدل ما هو في الشمال يروح يمين وهكذا

# B~ clear() تستخدم لحذف جميع عناصر ال list

# B~ copy() تستخدم لعمل نسخ من list الي list اخري

# B~ count() تستخدم لعد عنصر معين موجود كام مره

# B~ index() تستخدم للبحث عن رقم الانديكس بتاع العنصر الذي سوف تعطيه له يبحث في اول انديكس

# B~ insert() تستخدم لوضع عنصر معين قبل الانديكس الذي سوف تضعه

# B~ pop() تستخدم لوضع الانديكس ويرجع لك بقيمه هذا الانديكس

# B~ union() تستخدم لاتحاد او جمع بين اكثر من set

# B~ add() تستخدم لاضافه عنصر بداخل ال set

# B~ discard() تستخدم لحذف شي معين وحين عدم وجود العنصر الذي تريد حذفه لم يطبع ERROR

# B~ update() يعمل تحديث لل set من متغير ثاني

# B~ difference() تستخدم لمعرفه الاختلاف بين اي 2 set

# B~ difference() تستخدم لمعرفه الاختلاف بين اي 2 set

# B~ intersection() تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني

# B~ intersection_update()  تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني وتعمل تحديث للبيانات ويتم وضعهم في المتغير الاصلي

# B~ symmetric_difference() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود هنا ولبس موجود هنا

# B~ symmetric_difference_update() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود هنا ولبس موجود هنا وتعمل تحديث للمتغير الاصلي

# B~ issuperset() تستخدم لمعرف هل عناصر ال set نفس عناصر ال set الثانيه ام لا واذاك ان بعض العناصر موجوده بداخل ال set الثانيه سوف يرجع ب True

# B~ issubset() تستخدم لمعرفه هل ال set الاساسيه تساوي نفس عناصر ال set الثانيه

# B~ isdisjoint() تستخدم لمعرفه هل كل العناصر مختتلفه عن بعض

# B~ get() تستخدم للمناده علي ال key

# B~ setdefault() تستخدم لكي يبحث عن ال keys و value الذي سوف يتم وضعهم ان وجدهم سوف يرجع بيهم وان لم يلاقيهم سوف يعمل key جديده بال valuse الجديده

# B~ popitem() تستخدم لمعرفه اخر عنصر في المتغير

# B~ items() تستخدم لعرض ال keys و valuses حتي لو بعد عمل عنصر جديد

# B~ fromkeys(متغير ال value , متغير ال keys) يتم عمل Dictionary من خلالها ونستخدم قبلها .dict

# B~ range(1, 10, 2) تستخدم لوضع من اول رقم معين لحد رقم معين ويتم طبعتهم بشكل سليم
