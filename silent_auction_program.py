import os
def find_bidders(bidders_details):
    max_bid=0
    max_bidders=""
    
    for bidders in bidders_details:
        bidders_price=bidders_details[bidders]
        if max_bid<bidders_price:
            max_bidders=bidders
            max_bid=bidders_price        
    print(f"winner is {max_bidders} with a bid price of {max_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("enter your name\n")
    price=int(input("What is your bid\n"))
    bidder_data[name]=price

    more_bidders=input("Are there more bidders .Type 'yes' or 'No'\n").lower()
    if more_bidders == "no":
        end_of_bidding=True
        find_bidders(bidder_data)
    elif more_bidders =="yes":
        os.system('cls')  #for clear the windos
        