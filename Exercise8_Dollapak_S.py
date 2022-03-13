Username =input("Username :")
Password =input("Password :")
if Username == "admin" and Password == "1234":
    print("-X-X-X-X-X-X-X-X-X-X-X-")
    print("        Welcome        ")
    print("-X-X-X-X-X-X-X-X-X-X-X-")
    print("     product list      ")
    print("-----------------------")
    print("Cola            : 10THB")
    print("Lemon juice     : 15THB")
    print("Apple           : 20THB")
    print("-----------------------")
    item =input("What do you want to buy?")
    Many =(int(input("How many pieces do you want ?")))
    if item == "Cola":
        print(item, "X", Many, "total :",10*Many, "THB")
    elif item == "Lemonjuice":
        print(item, "X", Many, "total :",15* Many, "THB")
    elif item == "Apple":
        print(item, "X", Many, "total :",20* Many, "THB")
    else:
        print("Error")
elif Username == "admin" and Password != "1234":
    print("! Password Error !")
else:
    print("Please try again")
