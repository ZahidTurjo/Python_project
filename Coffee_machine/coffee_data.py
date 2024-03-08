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

x=input('Ebter the number ')
z=x.split(' ')
print(len(z))
for i in range(0,len(z)):
    z[i]=int(z[i])
print(z)    
sum=0
for i in z:
    sum+=i
    print(sum)

      