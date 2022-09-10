# Logical Operators
# Food = spaghetti laksa hamburger sate soto pizza donut vegetables

# Ask what is the persons favourite food & respond
fav_food = input("What is your favourite food?\n")
print("Ohhhhhh... " + fav_food + " you say!")

# Give a comment on the food depending on what it is = working
# if fav_food == "pizza":
#     print("Oh for sure ! How can you possible beat " + fav_food + " !!!")
# if fav_food == "spaghetti":
#     print("Oh for sure ! I cant get enough " + fav_food)
# if fav_food == "laksa":
#     print("Oh... I guess thats not too bad ")
# if fav_food == "hamburger":
#     print("Oh only if the " + fav_food + " comes from Burger King!")
# if fav_food == "sate":
#     print("Oh yeah ! My favourite is beef " + fav_food)
# if fav_food == "donut":
#     print("Ummm ! Actually I think that " + fav_food + " is too fattening")
# if fav_food == "vegetables":
#     print("Really? I didnt think you would like " + fav_food)

# adding Logical Operator = working with or operator
# if fav_food == "pizza" or fav_food == "sate":
#     print("Oh for sure ! How can you possible beat " + fav_food + " !!!")
# if fav_food == "spaghetti":
#     print("Oh for sure ! I cant get enough " + fav_food)
# if fav_food == "laksa":
#     print("Oh... I guess thats not too bad ")
# if fav_food == "hamburger":
#     print("Oh only if the " + fav_food + " comes from Burger King!")
# # if fav_food == "sate":
# #     print("Oh yeah ! My favourite is beef " + fav_food)
# if fav_food == "donut":
#     print("Ummm ! Actually I think that " + fav_food + " is too fattening")
# if fav_food == "vegetables":
#     print("Really? I didnt think you would like " + fav_food)

# Make sure they are talking about all or some laksa = working
# if fav_food == "pizza" or fav_food == "sate":
#     print("Oh for sure ! How can you possible beat " + fav_food + " !!!")
# if fav_food == "spaghetti":
#     print("Oh for sure ! I cant get enough " + fav_food)
# if fav_food == "laksa":
#     fav_laksa = input("Indo or Malay Laksa? ")
#     if fav_laksa == "Indo":
#         print("Yep, totally agree it's the tastiest!")
#     else:
#         print("You really need to try the Indonesian laksa !")
# if fav_food == "hamburger":
#     print("Oh only if the " + fav_food + " comes from Burger King!")
# if fav_food == "donut":
#     print("Ummm ! Actually I think that " + fav_food + " is too fattening")
# if fav_food == "vegetables":
#     print("Really? I didnt think you would like " + fav_food)
# else:
#     print("thats not a food I am familiar with, bring me some now !!")

# Describe the unknown food and reply
if fav_food == "pizza" or fav_food == "sate":
    print("Oh for sure ! How can you possible beat " + fav_food + " !!!")
if fav_food == "spaghetti":
    print("Oh for sure ! I cant get enough " + fav_food)
if fav_food == "laksa":
    fav_laksa = input("Indo or Malay Laksa? ")
    if fav_laksa == "Indo":
        print("Yep, totally agree it's the tastiest!")
    else:
        print("You really need to try the Indonesian laksa !")
if fav_food == "hamburger":
    print("Oh only if the " + fav_food + " comes from Burger King!")
if fav_food == "donut":
    print("Ummm ! Actually I think that " + fav_food + " is too fattening")
if fav_food == "vegetables":
    print("Really? I didnt think you would like " + fav_food)
else:
    print("I am not too familiar with that\n")
    spicy = input("Is it spicy? yes or no ")
    tastiness = int(input('On a score of Tastiness out of 10, what score would you give it? = '))
    if spicy == "no" and tastiness >5:
        print("Well I have to try that - go get me some !")
    else:
        print("Doesnt sound very interesting, dont give me any thanks")