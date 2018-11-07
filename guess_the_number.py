import random


class GuessTheNumber(object):
    """docstring for GuessTheNumber"""

    def __init__(self):
        self.random_number = random.randrange(0, 101)
        self.user_input = input

    def start_guess():
        random_number = random.randrange(0, 101)

        print("Random number has been generated.")

        while True:
            try:
                user_input = int(input("Your guess please: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if user_input == random_number:
                print("ell done! your guess is right")
                break

            elif not 0 <= user_input <= 100:    # If it's not between 0 to 100
                print("Our guess range is between 0 and 100, please try a bit {}."
                    # User_input at this point must be outside the range
                    # so if it's not below the min, it's definitely above the max
                     .format("higher" if user_input < 0 else "lower"))
            elif user_input <= random_number:
                print("wrong, your guess is lower")
                break
            else:
                if user_input >= random_number:
                    print("wrong, your guess is higher")
                    break


if __name__ == '__main__':
    GuessTheNumber.start_guess()
    print("End of program.")
