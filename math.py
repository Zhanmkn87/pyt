
print("")
print("МАТЕМАТИКA")
print("")

import random


x=1
while x != '2':

    operation = (input("ne esepteisyn? ( + , - , * , / ) "))
    quantity = int(input("neshe esep shigarasin? "))

    if operation == '/':
        correct = 0
        incorrect = 0
        for x in range (quantity):
            a = random.randint (50, 100)
            b = random.randint (1, 50)
            c = round(a/b, 1)
            print ("kansha boladi", a ,"/", b,)
            answer = eval(input("zhauap" ))
            if answer == c:
                print("duris!")
                correct = correct + 1
            if answer != c:
                print("kate,", "duris zhauap", c )
                incorrect = incorrect + 1
        print("sende", correct, "duris zhane ", incorrect, "kate")
        percent = correct/quantity*100
        if percent >= 90:
            print("baga 5!")
        elif percent >= 80:
            print("baga 4!")
        elif percent >= 70:
            print("baga3!")
        elif percent >= 60:
            print("baga 2!")
        else:
            print("baga 1!")

            


    if operation == '+':
        correct1 = 0
        incorrect1 = 0

        for x in range (quantity):
            a = random.randint (1, 100)
            b = random.randint (1, 100)
            c = a + b
            print ("kansha boladi", a ,"+", b,)
            answer = int(input("zhauap " ))
            if answer == c:
                print("duris!")
                correct1 = correct1 + 1
            if answer != c:
                print("kate,", "duris", c )
                incorrect1 = incorrect1 + 1

        print("sende", correct1, "duris zhane", incorrect1, "kate")

        percent = correct1 / quantity * 100
        if percent >= 90:
            print(" baga 5!")
        elif percent >= 80:
            print("baga 4!")
        elif percent >= 70:
            print("baga 3!")
        elif percent >= 60:
            print("baga 2!")
        else:
            print("baga 1!")



    if operation == '-':
        correct2 = 0
        incorrect2 = 0

        for x in range (quantity):
            a = random.randint (50, 100)
            b = random.randint (1, 50)
            c = a - b
            print ("kansha boladi", a ,"-", b,)
            answer = int(input("zhauap " ))
            if answer == c:
                print("duris!")
                correct2 = correct2 + 1
            if answer != c:
                print("kate,", "duris zhauap", c )
                incorrect2 = incorrect2 + 1

        print("sende", correct2, "duris zhane", incorrect2, "kate zhauap")

        percent = correct2 / quantity * 100
        if percent >= 90:
            print("baga 5!")
        elif percent >= 80:
            print("baga 4!")
        elif percent >= 70:
            print("baga 3!")
        elif percent >= 60:
            print("baga 2!")
        else:
            print("baga 1!")


    if operation == '*':
        correct3 = 0
        incorrect3 = 0

        for x in range (quantity):
            a = random.randint (1, 20)
            b = random.randint (1, 20)
            c = a * b
            print ("kansha boladi", a ,"*", b,)
            answer = int(input("zhauap " ))
            if answer == c:
                print("duris!")
                correct3 = correct3 + 1
            if answer != c:
                print("kate,", "duris zhauap", c )
                incorrect3 = incorrect3 + 1

        print("sende", correct3, "duris zhane", incorrect3, "kate zhauap")

        percent = correct3 / quantity * 100
        if percent >= 90:
            print("baga 5!")
        elif percent >= 80:
            print("baga 4!")
        elif percent >= 70:
            print("baga 3!")
        elif percent >= 60:
            print("baga2!")
        else:
            print("baga 1!")



