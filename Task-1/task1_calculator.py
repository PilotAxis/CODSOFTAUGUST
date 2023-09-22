print("---------------------------------------------------------------------")

print("~~~~~~~~~~~~~~~~~SIMPLE CALCULATOR USING PYTHON 3~~~~~~~~~~~~~~~~~~~~")

print("-----------------Task-1 CodSoft Internship August--------------------")

ans = 'y'
while ans == 'y':
    print("What type number do you want to input")
    print("Input 1 for INTEGERS")
    print("Input 2 for FLOATING POINT (Decimal)")

    choice = int(input("Enter 1 or 2 from the above choice :"))

    if choice == 1:
        print("Input two numbers below :-")
    
        a = int(input("Input your first number :-"))
        b = int(input("Input your second number :-"))

    elif choice == 2:
        print("Input two numbers below :-")
    
        a = float(input("Input your first number :-"))
        b = float(input("Input your second number :-"))

    print("Numbers you input are :-", a, "and", b)
    
    print("What type of arithmetic operations do you want?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus i.e %")

    ch = int(input("Enter 1,2,3,4,5 for desired arithmetic operations :"))

    if ch == 1:
        summ = a + b
        print("The sum of", a, 'and', b, "is", summ)
        ans = input("Want to calculate more press y or want to exit press n :")
        
    elif ch == 2:
        diff = a - b
        print("The difference of", a, 'and', b, "is", diff)
        ans = input("Want to calculate more press y or want to exit press n :")
        
    elif ch == 3:
        mult = a*b
        print("The product of", a, 'and', b, "is", mult)
        ans = input("Want to calculate more press y or want to exit press n :")
        
    elif ch == 4:
        div = a/b
        print("The division of", a, 'and', b, "is", div)
        ans = input("Want to calculate more press y or want to exit press n :")
        
    elif ch == 5:
        mod = a%b
        print("The mod of", a, 'and', b, "is", mod)
        ans = input("Want to calculate more press y or want to exit press n :")
        

print("Bye!, Thanks for using...")
    



