import random
number_digits = 4
list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter_tries_left = 10


def calculating_bulls_cows(guess_input: str, random_num: str, number_digits: int) -> tuple[int, int]:

    bulls = sum(1 for index in range(number_digits) if guess_input[index] == random_num[index])
    cows = sum(1 for digit in guess_input if digit in random_num) - bulls

    return bulls, cows
    # calculating bulls then cows


def yes_in_question(question: str) -> bool:
    return "yes" in question.lower()


def no_in_question(question: str) -> bool:
    return "no" in question.lower()


def end_in_guess(guess: str) -> bool:
    return "end" in guess.lower().strip()


def list_nums_range() -> bool:  # Deciding if the user wants to play with 0 and incrementing the length of the list then

    while True:
        question_for_0 = input("\n Would you like to play with the number - '0'?\n"
                               "Answer with 'yes' or 'no': ")

        if yes_in_question(question_for_0):
            return True

        elif no_in_question(question_for_0):
            return False

        else:
            print("\n Invalid input")


def generating_random_num(list_nums: list, number_digits: int) -> str:

    if including_0:
        list_nums.insert(0, 0)

    result = (random.sample(list_nums, number_digits))

    result = ''.join(map(str, result))

    return result


print("Welcome to the game of bulls and cows!\n"
      "Type in 'End' instead of a guess if you would like the program to finish manually.")

including_0 = list_nums_range()

random_num = generating_random_num(list_nums, number_digits)


while True:
    bulls = 0
    cows = 0
    guess_input = input("\n Type in your guess: ")

    if end_in_guess(guess_input):
        print("Game over. Stopped manually!")
        break

    elif len(guess_input) != number_digits or not guess_input.isdecimal() or len(set(guess_input)) != len(guess_input):
        print("\n Invalid input.")
        continue

    elif guess_input == random_num:
        print("Congratulations, you guessed the number!")
        break

    counter_tries_left -= 1

    if counter_tries_left == 0:
        print(f"You ran out of tries! Better luck next time! The number was {random_num}")
        break

    bulls, cows = calculating_bulls_cows(guess_input, random_num, number_digits)

    print(f"The number {guess_input} got {bulls} bulls and {cows} cows! {counter_tries_left} tries remaining.")
