#GAME STARTS
import random 
op = ["s","w","g"]

human_score = 0
computer_score = 0
chance = 3

print("Snake water gun")
print("s for snake-----w for water-----g for gun")

while chance>0:
    value = input("Snake, Water, Gun\n")
    _random = random.choice(op)

    if value==_random:
        print("There's a tie, zero points awarded\n")

    elif value=="s" and _random=="w":
        human_score = human_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You won, 1 point awarded")
        print(f"Your score is {human_score} and computer's score is {computer_score}")

    elif value=="w" and _random=="s":
        computer_score = computer_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You loose, 1 point awarded to computer")
        print(f"Your score is {human_score} and computer's score is {computer_score}")

    elif value=="g" and _random=="s":
        human_score = human_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You won, 1 point awarded")
        print(f"Your score is {human_score} and computer's score is {computer_score}")

    elif value=="g" and _random=="w":
        computer_score = computer_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You loose, 1 point awarded to computer")
        print(f"Your score is {human_score} and computer's score is {computer_score}")

    elif value=="s" and _random=="g":
        computer_score = computer_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You loose, 1 point awarded to computer")
        print(f"Your score is {human_score} and computer's score is {computer_score}")

    elif value=="w" and _random=="g":
        human_score = human_score + 1
        print(f"Your input is {value} and computer's input is {_random}")
        print("You won, 1 point awarded")
        print(f"Your score is {human_score} and computer's score is {computer_score}")


    else:
            print("Your input is wrong \n")

    chance = chance - 1


print("Game Over")
if computer_score==human_score:
    print("Tie")

elif computer_score > human_score:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"Final score: \n You score: {human_score} \n Computer score: {computer_score}")