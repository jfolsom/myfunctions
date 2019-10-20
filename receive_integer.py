def receive_integer():
    print('Enter a positive integer:')
    receivednumber = 'dummy'
    while receivednumber == 'dummy':
        try:
            receivednumber = int(float(input()))
            if not receivednumber > 0:
                print('That number is not positive.')
                continue
        except ValueError:
            print('That is not an integer.')
            continue
    print('Success:', receivednumber)
    return receivednumber