import random
def score_tracker(func):
    score = 0
    def wrapper():
        nonlocal score
        for _ in range(4):
            guess = func()
            if guess:
                score += 10 
            print(f"your score is {score}")
        result = print(f"Your final score is {score} /40!")
        return result
    return wrapper

@score_tracker
def guess_number():
    correct_number = random.randint(1, 10)
    num = int(input("Please enter your guess\n"))
    if num < 1 or num > 10:
        print("Please enter a valid number between 1-10")
        return False
    elif num == correct_number:
        print("You guessed correctly! You earned 10 points!")
        return True
    else:
        print(f"Your guess is incorrect. The correct number was {correct_number}")
        return False

guess_number()
