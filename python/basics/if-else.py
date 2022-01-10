while(True):
    #Get numeric value
    number = input("What is your number? ")
    number = int(number)

    #Check against threshold
    if (number > 100):
        print("You lyin', dawg.")
    elif (number < 0):
        print("You definitely lyin', dawg.")
    elif (number >= 65):
        print("You have passed!")
        break
    else:
        print("You have failed, try again...")
    print("\n")

print("\n")
print("Script terminated")
