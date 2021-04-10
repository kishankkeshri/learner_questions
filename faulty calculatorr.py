#suppose you are examiner like bhanu so you will circulate a faulty calculator which give 55 - 9=77 and rest other calculations will be correct
y_n = input("press y if you want to start calculation - ")
while y_n == "y":
    op = input("enter the operator\n"
               "'*' for multiplication\n"
               "'/' for division\n"
               "'+' for addition\n"
               "'-' for substraction\n")
    n1 = int(input("enter first number - "))
    n2 = int(input("enter second number - "))
    if n1 == 55 and n2 == 9 and op == "-":
        print("77")
    elif op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        print(n1 / n2)
    else:
        print("out of range")
    y_n = input("press y if you want to start calculation and n to stop - ")
    if y_n =="n":
        break