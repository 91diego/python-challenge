import random
import math

def generateArray(arrayLenght, multidimensional, multidimensionalQuantityElements):
    print(multidimensional)
    array_list = []
    if multidimensional:
        extraArrays = math.ceil(arrayLenght / multidimensionalQuantityElements)
        for i in range(int(extraArrays)):
            array_list.append([i for i in range(0, random.randint(1, arrayLenght))])
    else:
        array_list = [i for i in range(0, arrayLenght)]
    return [array_list, multidimensional]

def negativeNumbers(value):
    if value < 0:
        return True
 
def main():
    try:
        print("Welcome !!! ")
        arrayLenght = int(input("Put the maximum number to fill the array in random mode: "))
        if negativeNumbers(arrayLenght):
            arrayLenght = "error"
            multidimensional = "error"
            multidimensionalQuantityElements = "error"
            return 'Negative number is not valid'
        multidimensional = """
        Do you want to generate a multidimensional array?

        0.- No
        1.- Yes

        Please, choose an option """

        option = input(multidimensional)
        if option == 0:
            multidimensional = False
            multidimensionalQuantityElements = 0
        elif option == 1:
            multidimensional = True
            multidimensionalQuantityElements = int(input("Put the lenght of nested array:"))
            if negativeNumbers(arrayLenght):
                arrayLenght = "error"
                multidimensional = "error"
                multidimensionalQuantityElements = "error"
                return 'Negative number is not valid'
        else:
            print('Select a correct option')
    except ValueError:
        arrayLenght = "error"
        multidimensional = "error"
        multidimensionalQuantityElements = "error"
        print("Something was wrong! Please try again")
        return False

    array = generateArray(arrayLenght, multidimensional, multidimensionalQuantityElements)
    plain_array = []
    for x in range(0, len(array[0])):
        if(array[1]):
            for i in range(0, len(array[0][x])):
                plain_array.append(i)
        else:
            plain_array.append(x)
    return plain_array

if __name__ == '__main__':
    print(main())