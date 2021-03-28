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

options = [rock, paper, scissors]

computers_pick = random.randint(0, len(options)- 1)

user_pick = int(input("Pick a '0' for Rock, '1' for Paper, '2' for Scissors: \n"))


if user_pick >= len(options):
  print("You choose a number out of range of this game.")
else:
  if (user_pick == 0 and computers_pick == 2) or (user_pick == 2 and computers_pick == 1) or (user_pick == 1 and computers_pick == 0):
    print(f"{options[user_pick]} beats {options[computers_pick]}. User win!!!")
  elif user_pick == computers_pick:
    print("We have a tie.")
  else:
    print(f"{options[computers_pick]} beats {options[user_pick]}. Computer wins!!") 
