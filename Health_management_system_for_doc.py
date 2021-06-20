def getdate():
    import datetime
    return datetime.datetime.now()

def logInfo(number):
    if number == 1:             #For Food.
        h = ''' Choose the number for patient from below:
        1. Brijesh
        2. Yash
        3. Parth
        '''
        print(h)
        patientnumber = int(input("Enter the number of your patient: "))
        if patientnumber == 1:
            foodname = input("Enter the name of a food: ")
            with open("Brijesh-food.txt", "a") as f:
                f.write(f"{str(getdate())} : {foodname}\n")
                print(f"Food {foodname} has been successfully written in the list.\n")
        elif patientnumber == 2 :
            foodname = input("Enter the name of a food: ")
            with open("Yash-food.txt", "a") as f:
                f.write(f"{str(getdate())} : {foodname}\n")
                print(f"Food {foodname} has been successfully written in the list.\n")
        elif patientnumber == 3:
            foodname = input("Enter the name of a food: ")
            with open("Parth-food.txt", "a") as f:
                f.write(f"{str(getdate())} : {foodname}\n")
                print(f"Food {foodname} has been successfully written in the list.\n")

    elif number == 2:               #For Exercise.
        h = ''' Choose the number for patient from below:
        1. Brijesh
        2. Yash
        3. Parth
        '''
        print(h)
        patientnumber = int(input("Enter the number of your patient: "))
        if patientnumber == 1:
            exercisename = input("Enter the name of a exercise: ")
            with open("Brijesh-exercise.txt", "a") as f:
                f.write(f"{str(getdate())} : {exercisename}\n")
                print(f"Exercise {exercisename} has been successfully written in the list.\n")
        elif patientnumber == 2 :
            exercisename = input("Enter the name of a exercise: ")
            with open("Yash-exercise.txt", "a") as f:
                f.write(f"{str(getdate())} : {exercisename}\n")
                print(f"Exercise {exercisename} has been successfully written in the list.\n")
        elif patientnumber == 3:
            exercisename = input("Enter the name of a exercise: ")
            with open("Parth-exercise.txt", "a") as f:
                f.write(f"{str(getdate())} : {exercisename}\n")
                print(f"Exercise {exercisename} has been successfully written in the list.\n")


def retriveInfo(number):
    if number == 1:             #For Food.
        h = ''' Choose the number for patient from below:
        1. Brijesh
        2. Yash
        3. Parth
        '''
        print(h)
        patientnumber = int(input("Enter the number of your patient: "))
        if patientnumber == 1:
            with open("Brijesh-food.txt") as f:
                print(f.read())
        elif patientnumber == 2 :
            with open("Yash-food.txt") as f:
                print(f.read())
        elif patientnumber == 3:
            with open("Parth-food.txt") as f:
                print(f.read())


    elif number == 2:               #For Exercise.
        m = ''' Choose the number for patient from below:
        1. Brijesh
        2. Yash
        3. Parth
        '''
        print(m)
        patientnumber = int(input("Enter the number of your patient: "))
        if patientnumber == 1:
            with open("Brijesh-exercise.txt") as f:
                print(f.read())
        elif patientnumber == 2 :
            with open("Yash-exercise.txt") as f:
                print(f.read())
        elif patientnumber == 3:
            with open("Parth-exercise.txt") as f:
                print(f.read())


while(True):
    message = '''Hey doc, Welcome to your own Health Management System:
    Please choose an option to proceed:
    1. To log the patient's information: 
    2. To retrive the patient's information: 
    3. To exit the system.
    '''
    print(message)
    try:
        a = int(input("Enter your choice here: "))

        if a == 1:
            b = ''' Choose from below:
            1. Food
            2. Exercise
            '''
            print(b)
            c = int(input("Enter your choice: "))
            logInfo(c)

        elif a == 2:
            b = ''' Choose from below:
            1. Food
            2. Exercise
            '''
            print(b)
            c = int(input("Enter your choice: "))
            retriveInfo(c)

        elif a == 3:
            print("Have great day, Doc!!")
            exit()

    except ValueError as e:
        print("Choose a valid option")