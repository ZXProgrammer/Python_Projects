import os
import time

def start():
    print("\n")
    print("Welcome To Hangman\n\n")

def system_clear():
    time.sleep(1)
    os.system('clear')

def main():
    life = 7
    question = []
    answer = []

    start()

    game_setter = input("Set Word\n\n")
    hint_input = input("Enter Hint\n\n")

    system_clear()

    start()

    for letter in game_setter:
        answer.append(letter)

    for letter in answer:
        question.append("_")

    for _ in range(20):
        while True:
            print(f"Hint is:", hint_input)
            player_input = input("Enter any Letter\n\n") 
            if len(player_input) == 1:
                break
            else:
                print("Invalid input\n") 
            
        if player_input in answer:                
            for i in range(len(answer)):
                if answer[i] == player_input:
                    question[i] = player_input
                    print(question)
                
            if question == answer:
                print("You WON\n")
                break
        else:
            life = life - 1
            print(f"Incorrect Guess, Life = {life}\n\n")
            if life == 0:
                print("Game OVER\n")
                break

if __name__ == "__main__":
    main()

