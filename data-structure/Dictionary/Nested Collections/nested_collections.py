def nested_list_tuple():
    """
    List with nested tuples
    """

    user_list=[(1,2,3),(4,5,6)]

    print(user_list)

    print(user_list[1][2])
    print(user_list[0][1])
    print(user_list[0][1])

# o/p:
# [(1, 2, 3), (4, 5, 6)]
# 6
# 2
# 2


def nested_dictionary_tuple():
    """
    Dictionary with nested tuples
    """

    user_collection={'car':('merc','GT','BMW'),'watches':('Rolex','PP'),'shoes':('air','NB','Vans')}

    print(user_collection)

    print(user_collection['car'][1])
    print(user_collection['watches'][1])
    print(user_collection.get('shoes')[1])


def print_tuple():
    user_collection = {'cars': ('merc', 'GT', 'BMW'), 'watches': ('Rolex', 'PP'), 'shoes': ('air', 'NB', 'Vans')}

    for car in user_collection['cars']:
        print(car)



# Print Tuple
print_tuple()
print()


# Nested Dictionary-Tuple
nested_dictionary_tuple()
print()


# Nested List-Tuple :
nested_list_tuple()


