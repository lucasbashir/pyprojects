import sys

while True: # Main program loop
    while True: # Keep asking until the user enters valid input
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break # Exit the loop when the user enters a valid number
        print('Please enter a number greater than 0, or QUIT.')
    print()

    #checking if user enters one or two

    if nth == 1:
        print('0')
        print()
        print("the #1 fibonacci number is 0")
        continue
    elif nth == 2:
        print('0', '1')
        print()
        print("The second fibonacci number is 1")
        continue
    if nth >= 1000:
        print("WARNING!: This will take a while to display on the screen")
        print("Press Ctrl-C if you want to quit")
        input('Press enter to begin')

    #calculate the nth fibonacci number
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')

    # Display all the later numbers of the Fibonacci sequence
    while True:
        nextNumber =secondToLastNumber + lastNumber
        fibNumbersCalculated += 1
        # Display the next number in the sequence
        print(nextNumber, end='')
        
        # Check if we've found the Nth number the user wants:
        if fibNumbersCalculated == nth:
            print()
            print()
            print(f"The #{fibNumbersCalculated} Fibonacci number is {nextNumber}", sep='')
            break
        # Print a comma in between the sequence numbers:
        print(', ', end='')
        # Shift the last two numbers:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
