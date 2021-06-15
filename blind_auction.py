from replit import clear


auction_dict = {}


def find_highest_bidder(group_of_bidders):
  highest_bid = 0
  winner = ""
  for bid in group_of_bidders:
    money = group_of_bidders[bid]
    if money > highest_bid:
      highest_bid = money
      winner = bid
  print(f"The winner is {winner} with a bid of ${highest_bid}.")


def blind_auction():
  start_over = False
  while not start_over:
    name = input("Please add your name: \n")
    bid_amount = int(input("Now place you bid amount: \n"))
    auction_dict[name] = bid_amount
    add_bidders = input("Are there anyone else that wants to join this bid? yes/no \n").lower()
    if add_bidders == "no":
      start_over = True
      find_highest_bidder(auction_dict)
    elif add_bidders == "yes":
      clear()
      
      

blind_auction()