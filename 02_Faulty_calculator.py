#https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-15


try:
    operator = input("Choose operator from one of this '+' , '-' , '*' , '/' : ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if operator == '+':
        if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
            print("77")
        else:
            print(f"{num1+num2}")
    
    elif operator == '-':
        print(f"{num1-num2}")

    elif operator == '*':
        if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
            print("555")
        else:
            print(f"{num1*num2}")
    
    elif operator == '/':
        if num1 == 56 and num2 == 6 or num1 == 6 and num2 == 56:
            print("4")
        else:
            print(f"{num1/num2}")

except ValueError as e:
    print("Choose valid values.")