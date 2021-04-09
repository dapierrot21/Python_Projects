def prime_checker(number):
  is_prime = True
  # Prime numbers are numbers that can only be cleanly divided by itself and 1.
  for n in range(2, number): # all number are divisible by 1.
    if number % n == 0:
      is_prime = False # triggers the end of the for loop.
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")