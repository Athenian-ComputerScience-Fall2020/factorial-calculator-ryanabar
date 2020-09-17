# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  None

def factorial_calc(num):   #you may choose the name of the parameter

    factorial = 1

    if num < 0:
        print("Factorial does not exist for any negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        for x in range(1, num + 1):
            factorial = x * factorial
    return factorial

if __name__ == '__main__':

    num = int(input("Enter value to factorialize: "))
    
    # Test your code with this first
    # Change the argument to try different values
    print(factorial_calc(num))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
