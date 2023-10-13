function = input("What function would you like to preform? ")
bob = "james"
while bob == "james":
    if (function.lower() == "string format"):
        stringFormatted = """Twinkle, twinkle, little star,
        How I wonder what you are! 
            Up above the world so high,         
            Like a diamond in the sky. 
    Twinkle, twinkle, little star, 
        How I wonder what you are"""
        print(stringFormatted)
        function = input("What function would you like to preform? ")
    elif (function.lower() == "generate list and tuple"):
        num = True
        list1 = [""]
        tuple1 = ("")
        setNum = input("Input the set of values you would like to convert (seperate values by a comma): ")
        setNum = setNum.replace(",", "")
        list1 = setNum.split()
        print("List : " + str(list1))
        print("Tuple : " + str(tuple(list1)))
        function = input("What function would you like to preform? ")
    elif (function.lower() == "vowel"):
        letter = input("Enter any letter and check if it is a vowel or not: ")
        if (letter == "a"):
            print("True")
        elif (letter == "e"):
            print("True")
        elif (letter == "i"):
            print("True")
        elif (letter == "o"):
            print("True")
        elif (letter == "u"):
            print("True")
        else:
            print("False")
        function = input("What function would you like to preform? ")
    elif (function.lower() == "sort list"):
        values = input("Input the set of values you would like to convert (seperate values by a space): ")
        values = values.replace(",", "")
        list2 = values.split()
        finalList = []
        for x in list2:
            if (x == "237"):
                break
            elif (int(x) % 2 == 0):
                finalList.append(int(x))
        print(finalList)
        function = input("What function would you like to preform? ")
    elif (function.lower() == "common list"):
        commonList = []
        firstList = input("Input the first list of items you would like to compare: ")
        secondList = input("Input the second list of items you would like to compare: ")
        firstList = firstList.replace(",", "")
        aList = firstList.split()
        secondList = secondList.replace(",", "")
        bList = secondList.split()
        for x in aList:
            for y in bList:
                if (x == y):
                    commonList.append(int(x))
        newSet = set(commonList)
        finalList = list(newSet)
        print(sorted(finalList))
        function = input("What function would you like to preform? ")
    elif (function.lower() == "end"):
        bob = "not james"
