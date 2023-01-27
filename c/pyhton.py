print("you spawn in a island do you want to find shelter")
user = input ("yes/no")

if user == "yes": 
    print("you have shelter, but you are low on food, do you want to go hunting")
    user = input ("yes/no")
    if user == "yes":
        print("you have gotton food it is getting dark do you want to make a fire")
    elif user == "no":
        print("while sitting in your shelfter a bear comes and eats you")    

elif user == "no":
    print("you have no shelter, would you reather go hunting for food")
    user = input ("yes/no")
    if user == "yes":
        print("you have food, it is getting dark do you want to make a fire")
    elif user == "no":
        print("you die")