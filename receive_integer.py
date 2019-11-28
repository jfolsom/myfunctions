def receive_integer():

    while True:
        print('Enter a positive integer:')
        try:
            userinput = int(float(input()))
        except ValueError:
            print('Python can\'t make an integer out of that.')
            print('Maybe you used a comma in your number? That\'s')
            print('too fancy for me.')
            continue
        if isinstance(userinput, int) and userinput > 0:
            return userinput
            break
        else:
            print("That number is not positive.")


userinteger = receive_integer()
print(userinteger)
