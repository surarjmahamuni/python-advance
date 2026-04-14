def store_description():


    supermarket={
                'first_store':{
                    'name':'Macys Store',
                    'items':[
                        {'name':'Levis Jeans','quantity':5},
                        {'name':'Polo Tshirt','quantity':10},
                        {'name':'nike shoe','quantity':10},
                        {'name':'nike shoes','quantity':12},
                    ]

                },
                'second_store':{
                    'name':'Ralphs Store',
                    'items':[
                        {'name':'Pepsi','quantity':110},
                        {'name':'Milk','quantity':'22'},
                        {'name':'Water','quantity':26}
                    ]

                }
    }

    num=input("Enter the store number: first_store or second_store: ")

    print(f"Store name is {supermarket[num]['name']}")
    print("Items present in the store and their quantity:")
    for item in supermarket.get(num).get('items'):
        print(f"{item.get('name')} has {item.get('name')} quantity")


store_description()