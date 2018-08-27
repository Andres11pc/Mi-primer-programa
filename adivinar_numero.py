
number_to_guess = 4

user_number = int(input('Adivina un numero: '))

if number_to_guess == user_number:
    print('Has ganado')
else:
    print('Has perdido')

    while user_number != number_to_guess:
        print('Vuelve a intentarlo')

        user_number = int(input('Adivina un numero: '))

        if number_to_guess == user_number:
            print('Has ganado')
        else:
            print('Has perdido')
