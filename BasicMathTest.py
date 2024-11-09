import random
import time
OPERANDS = ["+", "-", "*"]
minimum_number = 3
maximum_number = 12

left_number = random.randint(minimum_number, maximum_number)
right_number = random.randint(minimum_number, maximum_number)
operand = random.choice(OPERANDS)
maximum_number_of_questions = 7
def generate_questions():
    expression = str(left_number) + operand + str(right_number)
    answer = eval(expression)

    return expression, answer
wrong_guesses = 0


starting_time = time.time()
for numbers in range(maximum_number_of_questions):
        left_number = random.randint(minimum_number, maximum_number)
        right_number = random.randint(minimum_number, maximum_number)
        operand = random.choice(OPERANDS)
        maximum_number_of_questions = 7
        generate_questions()
        expression, answer = generate_questions()
        while True:
            question = input(f"#{numbers+1} {expression}: ")
            if question == str(answer):
                break
            else:
                 wrong_guesses += 1
ending_time = time.time()

time_it_took_to_complete = round(ending_time - starting_time, 1)

if wrong_guesses == 0:
     print("Wow, you did not fail any questions, keep it up!!!")
else:
     print(f"You had {wrong_guesses} retries.")
print(f"It took you {time_it_took_to_complete} seconds to complete.")
