import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


expression = [rock, paper, scissors]
user_input = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(expression[user_input])
computer_input = random.randint(0, 2)
print(f"Computer chosses:")
print(expression[computer_input])


if user_input >= 3 or user_input > 0:
  print("You put invalid no. You lost!")
elif user_input == 0 and computer_input == 2:
  print("You Win!")
elif computer_input > user_input:
  print("You Lost!")
elif computer_input == user_input:
  print("Its a Draw!")
elif computer_input == 0 and user_input == 2:
  print("You Lost!")
elif user_input > computer_input:
  print("You Win!")
