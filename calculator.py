def PythonCalculator():
    numOne= int(input("Please Enter number 1: "))
    numTwo= int(input("Please Enter number 2: "))

    operand = int(input("Enter the Operand '\n' 1:add '\n' 2:subtract '\n' 3:multiply,'\n' 4:divide: '\n' "))

    if operand ==1:
        return numOne + numTwo
    elif operand ==2:
        return numOne - numTwo
    elif operand ==3:
        return numOne * numTwo
    elif operand == 4:
        return numOne + numTwo
    else:
        return "You entered the wrong operand"

if __name__ == "__main__":
    result = PythonCalculator()
    print(result)