import addition
import subtraction
import multiplication
import division

print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")


while True:
    action = input("Please enter your selection (1/2/3/4): ")
    if action in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Please enter first number: "))
            num2 = float(input("Please enter second number: "))
        except ValueError:
            print ("You have typed the wrong number!")
        if action == '1':
            print(num1, "+", num2, "=", addition.add_two_numbers(num1, num2))

        elif action == '2':
            print(num1, "-", num2, "=", subtraction.subtract_two_numbers(num1, num2))

        elif action == '3':
            print(num1, "*", num2, "=", multiplication.multiply_two_numbers(num1, num2))

        elif action == '4':
            if (num2 == 0):
                print("Sorry! You can not devide by 0")
            print(num1, "/", num2, "=", division.divide_two_numbers(num1, num2))
            
        else:
            print("Invalid input!")

        print("Yes = Y")
        print("No = N")
        next_action = input("Let's do next calculation? (Yes / No): ")
        
        if next_action == 'Y':
            continue
        
        elif next_action == 'N':
            print('See you next time!')
            break


        else:
            print("You have typed invalid input!")
    