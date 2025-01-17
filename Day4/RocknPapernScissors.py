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

user_input = input("Pick a choice: 1. rock, 2. paper, 3. scissors: ")

if user_input == '1':
    print(rock)
elif user_input == '2':
    print(paper)
else:
    print(scissors)

print("Computer Choice")
comp_input = random.randint(1,3)
if user_input == '1':
    print(rock)
elif user_input == '2':
    print(paper)
else:
    print(scissors)

if user_input == '1' and comp_input == '1':
    print("you draw")
elif user_input == '1' and comp_input == '2':
    print('You lose')
elif user_input == '1' and comp_input == '3':
    print('You win')

elif user_input == '2' and comp_input == '1':
    print("you Win")
elif user_input == '2' and comp_input == '2':
    print('You draw')
elif user_input == '2' and comp_input == '3':
    print('You lose')

elif user_input == '3' and comp_input == '1':
    print("you lose")
elif user_input == '3' and comp_input == '2':
    print('You win')
else:
    print('You Draw')