try:
    n = int(input("Enter your age or the year you were born: "))
    if len(str(n)) == 2 or len(str(n)) == 1:
        age = n
        print(f"Your age is {age} today!!")
        yearofborn1 = 2021 - age
        print(f"after {100-age} years later in {yearofborn1+100}, You will turn 100 years old!")

    elif len(str(n)) == 4:
        yearofborn = n
        if yearofborn < 2021:
            age1 = 2021- yearofborn
            print(f"You were born in {yearofborn} and your age is {age1}.")
            print(f"after {100-age1} years in {yearofborn+100}, you will be 100 years old!")
        elif yearofborn>2021:
            print("You have not born yet.")

    elif len(str(n)) !=1 or 2 or 4:
        print("This value does not define your age or the year you were born, please try again.")
        
except ValueError as e:
    print("Enter a valid value.")