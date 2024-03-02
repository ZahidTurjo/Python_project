menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":100,
    },

    "latte":{
        "ingredients":{
            "water":200,
            'milk':150,
            "coffee":24
        },
        "cost":150,
    },    
    "cappuccino":{
        "ingredients":{
            "water":250,
            'milk':100,
            "coffee":28
        },
        "cost":200,
    },    
    
}

resources={
    'milk':500, 
    "water":1000,
    'coffee':100
}

def check_resources(ordered_ingredients):
    for item in ordered_ingredients: 
        if ordered_ingredients[item]>resources[item]:
            print(f"Insufficient of resources{item}")
            return False
    return True

def process_coins():
    print('Please Insert Coins')
    total=0
    coins_five=int(input("how many 5 taka coins :"))
    coins_ten=int(input("how many 10taka coins :"))
    coins_twenty=int(input("how many 20 taka coins :"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total

def is_payment_successful(recived_money,ordered_money):
    global profit
    if recived_money>=ordered_money:
        profit+=ordered_money
        print(f"Here is your change {recived_money-ordered_money} taka")
        return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False
        
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕....Enjoy💁🏼")

profit=0
is_on=True
while is_on:
    choice=input("What would you like to have?(latte/espresso/cappuccino):")
    if choice == 'off':
        is_on=False
    if choice == "report":
        print(f"Water= {resources['water']} ml")
        print(f"milk= {resources['milk']} ml")
        print(f"coffee= {resources['coffee']} ml")
        print(f"Money= {profit} taka")

    else:
        coffee_type=menu[choice]   
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])