# Math QUIZ Practice
import random
from sympy import symbols, solve
import time


# check if user input is a valid digit
def check_digit(input_string, first_range, last_range):
    list_of_options = []
    for numbers in range(first_range, last_range + 1):  # add all possible options in list
        list_of_options.append(numbers)
    if (input_string.isdigit()):  # check if string is digit
        for number in list_of_options:  # check if string is in the list of options
            if (number == int(input_string)):
                return True
    else:
        return False


# quadratic function
def quadratic(difficulty):
    solution_list = []  # solution list
    x = symbols('x')

    # djfferent difficulty levels
    if (difficulty == 1):

        solution1 = random.randint(-10, 10)  # randomize solutions
        solution2 = random.randint(-10, 10)

        # set up and organize the values
        a_coefficient = 1

        b_coefficient = solution1 + solution2
        c_coefficient = solution1 * solution2

        solution_list.append(solution1)  # add solution to solution list
        solution_list.append(solution2)

    elif (difficulty == 2):

        solution1 = random.randint(-100, 100) / 10  # randomize solutions
        solution2 = random.randint(-100, 100) / 10

        # set up and organize the values
        a_coefficient = 1

        b_coefficient = solution1 + solution2
        b_coefficient = round(b_coefficient, 2)

        c_coefficient = solution1 * solution2
        c_coefficient = round(c_coefficient, 2)

        solution_list.append(solution1)  # add solution to solution list
        solution_list.append(solution2)

    else:
        a_coefficient = random.randint(-15, 15)  # randomize coefficients
        b_coefficient = random.randint(-15, 15)
        c_coefficient = random.randint(-15, 15)

        # the expression and it's solution
        expr = (a_coefficient) * x * x + (b_coefficient) * x + (c_coefficient)
        sol = solve(expr)

        # add the solutions to the solution list
        for answer in sol:
            answer = round(answer, 2)
            solution_list.append(answer)

    # print the problem and ask for user input
    print(f'\nThe question is: {a_coefficient}x^2 + {b_coefficient}x + {c_coefficient}')

    # option display
    if (option_display(quadratic, difficulty) == False):
        return None

    answer = input("\nWhat is your answer? Round to the hundredth and split the answer with comma: ")

    # split user input into list
    user_list = answer.split(',')

    # check if answer is correct
    for answer in user_list:
        answer = str(answer)
        if (answer == str(solution_list[0]) or answer == str(solution_list[1])):
            correct = True
        else:
            correct = False
            break

    if (correct == False):
        print(f"\nIncorrect. The correct answers are {solution_list[0]} and {solution_list[1]}")

    else:
        print("\nCorrect")

    return None


# mental math function
def mental_math(difficulty):
    user_list = []  # user input list
    answer_list = []  # answer list

    print(
        "\nIn this quiz, you will be timed and given ten questions to answer. Score a 10/10 to have your time recorded")

    # option display
    if (option_display(mental_math, difficulty) == False):
        return None

    # question loop
    start = time.perf_counter()  # starts timer
    questions = 0
    while questions <= 10:
        types = random.randint(1, 3)
        if (types == 1):  # first type of questions are multiplication questions
            if (difficulty == 1):
                first_number = random.randint(1, 12)
                second_number = random.randint(1, 12)
                third_number = 1
            elif (difficulty == 2):
                first_number = random.randint(-12, 12)
                second_number = random.randint(-12, 12)
                third_number = 1
            else:
                first_number = random.randint(-12, 12)
                second_number = random.randint(-12, 12)
                third_number = random.randint(-12, 12)

            # ask user the question and record data into list
            user_input = input(f"\n{first_number} * {second_number} * {third_number} = ?\nEnter here: ")
            user_list.append(user_input)
            answer = first_number * second_number * third_number
            answer_list.append(answer)

        elif (types == 2):  # second type of questions are division questions
            if (difficulty == 1):
                first_number = random.randint(1, 144)
                second_number = random.randint(1, 12)
            elif (difficulty == 2):
                first_number = random.randint(1, 1000)
                second_number = random.randint(-12, 12)
            else:
                first_number = random.randint(-12, 12)
                second_number = random.randint(-12, 12)

            # ask user the question and record data into list
            user_input = input(f"\nHow many times can {second_number} go into {first_number}?\nEnter here: ")
            user_list.append(user_input)
            answer = first_number // second_number
            answer_list.append(answer)

        else:  # last type if questions are adding and subtracting
            if (difficulty == 1):
                first_number = random.randint(0, 100)
                second_number = random.randint(0, 100)
            elif (difficulty == 2):
                first_number = random.randint(-200, 200)
                second_number = random.randint(-200, 200)
            else:
                first_number = random.randint(-1000, 1000)
                second_number = random.randint(-1000, 1000)

            # ask user the question and record data into list
            user_input = input(f"\n{second_number} + {first_number} = ?\nEnter here: ")
            user_list.append(user_input)
            answer = first_number + second_number
            answer_list.append(answer)

        questions += 1

    end = time.perf_counter()  # end timer
    time_ = (start - end)
    time_ = round(time_, 4) * -1

    # check if user input is correct or wrong
    i = 0
    correct_answer = 0
    while i != 10:
        if (user_list[i].isdigit()):
            if (int(user_list[i]) == int(answer_list[i])):
                correct_answer += 1
            else:
                print(f"\nQuestion {i}, you answered {user_list[i]}, the correct answer is {answer_list[i]}")
        else:
            print(f"\nQuestion {i}, you answered {user_list[i]}, the correct answer is {answer_list[i]}")
        i += 1

    # displays score and time
    print(f"\nYour time is {time_} seconds and you got {correct_answer}/10 questions correct")


# trigonometry function
def trig(difficulty):
    if (difficulty == 1):
        # randomize numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)

        print(f"\nThe cosine is {num1}/{num3} and the sine is {num2}/{num3}. What is the tangent?")

        # option display
        if (option_display(trig, difficulty) == False):
            return None

        user_input = input("Write answer as fractions \nEnter here: ")

        # check if user input is correct
        if (str(user_input) == str(num2 / num1)):
            print("\nCorrect!")
        else:
            print(f"\nIncorrect. The answer is {num2}/{num1}")

    elif (difficulty == 2):
        question_type = random.randint(1, 3)

        print('''\n
            |\ 
            | \ 
            |  \  
          x |   \   z 
            |    \ 
            |     \ 
            |     O\ 
            --------  
                y 
        ''')

        if (question_type == 1):
            # randomize  numbers
            x = random.randint(1, 100)
            y = random.randint(1, 100)

            print(f"\nWhat is the tangent of angle O when x = {x} and y = {y}?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input("\nWrite in fraction\nEnter here: ")

            # check if user input is correct
            if (str(user_input) == str(f"{x}/{y}")):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer was {x}/{y}")


        elif (question_type == 2):
            x = random.randint(1, 100)
            z = random.randint(1, 100)

            print(f"\nWhat is the sine of angle O when x = {x} and z = {z}?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input("Write in fraction\n Enter here: ")

            # check if user input is correct
            if (str(user_input) == str(f"{x}/{z}")):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer was {x}/{z}")

        else:
            y = random.randint(1, 100)
            z = random.randint(1, 100)

            print(f"\nWhat is the cosine of angle O when x = {y} and y = {z}?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input("\nWrite in fraction\nEnter here: ")

            # check if user input is correct
            if (str(user_input) == str(f"{y}/{z}")):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer was {y}/{z}")

    else:
        list_of_angle = [0, 30, 45, 60, 90]
        cos_list = [1, 3 / 2, 2 / 2, 1 / 2, 0]
        sin_list = [0, 1 / 2, 2 / 2, 3 / 2, 1]
        tan_list = [0, 3 / 3, 1, 3 / 1, "undefine"]
        angle = random.randint(0, 4)
        problem_type = random.randint(1, 3)

        if (problem_type == 1):

            print(f"\nWhat is the cosine of {list_of_angle[angle]} degree?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input("\nIf the final answer contains radical, ignore the radical.\nEnter here: ")

            # check if user input is correct
            if (user_input == str(cos_list[angle])):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer is {cos_list[angle]}")

        elif (problem_type == 2):

            print(f"\nWhat is the sine of {list_of_angle[angle]} degree?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input("\nIf the final answer contains radical, ignore the radical.\nEnter here: ")

            # check if user input is correct
            if (user_input == str(sin_list[angle])):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer is {sin_list[angle]}")

        else:

            print(f"\nWhat is the tangent of {list_of_angle[angle]} degree?")

            # option display
            if (option_display(trig, difficulty) == False):
                return None

            user_input = input(
                "\nIf the final answer contains radical, ignore the radical. If no answer, write 'undefine'\nEnter here: ")

            # check if user input is correct
            if (user_input == str(tan_list[angle])):
                print("\nCorrect!")
            else:
                print(f"\nIncorrect. The correct answer is {tan_list[angle]}")

    # while loop to ask if use want to practice again
    while True:
        user_input = input("\n1. Again?\n2. Quit\nEnter here: ")
        if (check_digit(user_input, 1, 2)):
            break
        print("\nPlease enter vaild number")

    if (int(user_input) == 1):
        trig(difficulty)
    else:
        return None


# option display menu
def option_display(unit, difficulty):
    while True:
        option = input(
            "\nWhat would you like to do?\n1. Answer/Start \n2. Hint\n3. New Question\n4. Return to main menu\nEnter here: ")
        if (check_digit(option, 1, 4)):
            option = int(option)
            if (option == 1):
                return None
            elif (option == 2):
                hint(unit, difficulty)  # calls hint function
            elif (option == 3):
                if (unit == quadratic):
                    quadratic(difficulty)  # calls quadratic function
                elif (unit == mental_math):
                    mental_math(difficulty)  # calls mental_math function
                else:
                    trig(difficulty)
            else:
                return False
        else:
            print("\nPlease enter a valid number")
    return None


# hint function that gives hint to user
def hint(unit, difficulty):
    if (unit == quadratic):
        if (difficulty == 1):
            print("\nAnswers add up to B-Coefficient and multiply to C-Coefficient")
        elif (difficulty == 2):
            print("\nA-Coefficient times C-Coefficient")
        else:
            print("\nQuadratic Formula")
    elif (unit == mental_math):
        print("\nJust some mental maths")
    else:
        print("\nSoh Cah Toa")
    return None


# main loop
run = True
while run:

    # user input math topic
    option = input(
        "\nWhich topic do you want to practice on?\n1. Quadratic\n2. Mental Math\n3. Trigonometry\n4. Quit\nEnter here: ")

    if (check_digit(option, 1, 4)):  # check if user input is a vaild digit
        if int(option) == 4:  # if user select option 4, exit loop
            run = False
        else:
            # user input math difficulty
            difficulty = input("\nSelect a difficulty\n1. Easy\n2. Medium\n3. Hard\nEnter here: ")

            if check_digit(difficulty, 1, 3):

                # change option and difficulty into integers
                option = int(option)
                difficulty = int(difficulty)

                # calls respective math topic function
                if (option == 1):
                    quadratic(difficulty)
                elif (option == 2):
                    mental_math(difficulty)
                else:
                    trig(difficulty)

            else:
                print("\nPlease enter a valid number")

    else:
        print("\nPlease enter a valid number")

print("System Exiting... Completed")