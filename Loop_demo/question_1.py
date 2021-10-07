while 1:
    for random_number in range(1, 3):
        print("Enter your number from 1 to 3:")
        guess_number = input()
        if int(guess_number) == random_number:
            print("You won!! you guess {0} and the number was {1}".format(guess_number, random_number))
            break
        else:
            print("You Loose!! you guess {0} and the number was {1}".format(guess_number, random_number))