from art import logo
print(logo)

def find_highest(bidding_records: dict):
    highest = 0
    winner = ""
    for bidder in bidding_records:  #cycle to iterate through the bidders
        bid_amount = bidding_records[bidder]    #getting the bid_amount of every bidder
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest}")

dictionary = {}
continue_bidding = True #condition to stay in the cycle
while continue_bidding:
    name = str(input("What is your name?\n"))   #getting the name of the bidder
    bid = int(input("What is your bid?\n$"))    #getting bidder's bid

    dictionary[name] = bid #saving value in dictionary

    new_bidder = str(input("Are there any other bidders? Type 'yes or 'no'."))  #asking if there are any other bidders

    if new_bidder == "no":  #if no the cycle ends
        continue_bidding = False
    elif new_bidder == "yes":   #if yes the screen clears
        print("\n" * 25)

find_highest(dictionary)    #calling the function to find the winner