import random
print("Welcome to Rock, Paper, Scissor Game!🎮")
choices=["rock", "paper", "scissor"]
end= "exit"

while True:
    user_choice= input(f"Enter your choice: {choices} and if you want to exit game enter 'exit' to quit: ").lower()
    if user_choice==end:
        print("Thanks for playing🎮, Good byee!!")
        break
    elif user_choice not in choices:
       print("Invalid choice, please try again!")
       continue
    else:
        computer_choice=random.choice(choices)
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice:{user_choice}")
        if user_choice==computer_choice:
            print("Its a tie!🤝")
        elif user_choice=="rock" and computer_choice=="scissor":
            print("You win!🎉")
        elif user_choice=="paper" and computer_choice=="rock":
            print("You win!🎉")
        elif user_choice=="scissor" and computer_choice=="paper":
            print("You win!🎉")
        else:
            print("You lose😞, computer win!")