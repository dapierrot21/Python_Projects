#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the Tip Calculator. \n")

bill = float(input("How much is the total bill?: $"))
tip = int(input("Please pick a percentage you would like to give? 10, 12, 15, etc: "))
bill_split = int(input("How many people are splitting the bill?: "))
new_bill = tip / 100 * bill + bill
bill_per_person = new_bill / bill_split

print(f"Each person should pay: ${round(bill_per_person, 2)}")