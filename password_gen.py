#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input(f"How many letters would you like in your password? Range: {len(letters)}\n")) 
nr_symbols = int(input(f"How many symbols would you like? Range: {len(symbols)}\n"))
nr_numbers = int(input(f"How many numbers would you like? Range: {len(numbers)}\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

if nr_letters > len(letters):
  print(f"Your choose was out of range of the options. Please pick within {len(letters)} letters.")
if nr_symbols > len(symbols):
  print(f"Your choose was out of range of the options. Please pick within {len(symbols)} symbols.")
if nr_numbers > len(numbers):
    print(f"Your choose was out of range of the options. Please pick within {len(numbers)} numbers.")
else:
  num_letters = nr_letters
  num_symbols = nr_symbols
  num_numbers = nr_numbers

  letter_pass = ''.join(random.choice(letters) for l in range(0, num_letters + 1))
  symbol_pass = ''.join(random.choice(symbols) for l in range(0, num_symbols + 1))
  number_pass = ''.join(random.choice(numbers) for l in range(0, num_numbers + 1))

  new_password = letter_pass + symbol_pass + number_pass
  new_password = list(new_password)
  random.shuffle(new_password)

  
  secret_password = ''.join(random.choice(new_password) for l in range(0, len(new_password)))

  print(f"This is your password: {secret_password}")

