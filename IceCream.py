#Favorite Ice Cream & Film Scene
#John Hatch

def flavor():   #The Main Function
    x = 0
    c = "chocolate"
    hints = ["It is a very popular flavor", "It can be made with nuts", "It can be either milk or dark", "It rhymes with pocolate"]
    for i in hints:
        uchoice = input("Guess my favorite ice cream flavor sunny boy. ").lower()
        if uchoice == c:
            print("Well played young blood, that's my favorite flava especially on a hot day")
            break
        else:
            print("Guess again broheim")
            print(hints[x + 1])
            x = x+1
flavor()
            





