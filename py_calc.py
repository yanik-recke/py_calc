
def convert():
    convert = input("Convert to HEX or DEC? ")

    if(convert == "HEX"):
        return (hex(int(input())))

    elif(convert == "DEC"):
        return (int(input(),16))

    elif(convert == "q"):
        return "q"
        


def calc():
    print("Only accepts hex numbers as operators")
    op1 = input("Operator 1: ")
    operation = input("Operation (ADD, SUB): ")
    op2 = input("Operator 2: ")


    if(operation == "ADD"):
        return (int(op1, 16) + int(op2, 16))

    elif(operation == "SUB"):
        return (int(op1, 16) + int(op2, 16))


def show_help():
    print()
    print("HELP page")
    print("ca = calculate")
    print("co = convert to hex or decimal number")
    print("Calculation only works with hex numbers, for calculation of decimal numbers use a calculator")
    print("You can either convert to decimal number or hex number, to convert to decimal enter DEC, for hex enter HEX.")
    print()
    


call = "!q"

while(call != "q"):
    call = input("CALC (ca) or CONVERT (co)\n")
    
    if(call == "ca"):
        result = calc()
        print(result)

    elif(call == "co"):
        result = convert()
        print(result)

    elif(call == "help"):
        show_help()
