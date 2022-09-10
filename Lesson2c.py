teacher = "Mr Tory, Mr Shane, Ms Lya, Ms Tri"
print("Who is your favourite teacher from the following list? \n" + teacher)
fav = input("Type your choice here \n")

#print("Yes I agree that " + fav + "is pretty cool!")
#Demo without exit() first
if fav == "Mr Tory":
    print("Yeah he is always smiling")
    exit()
if fav == "Mr Shane":
    print("Yeah but he is always late!")
    exit()
if fav == "Ms Lya":
    print("yes, she is always on time")
    exit()
if fav == "Ms Tri":
    print("Yep - she really knows math well !")
    exit()
else:
    print("Oh!, " + fav + "is a teacher i have never heard of?")
