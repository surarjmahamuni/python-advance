import json
from typing import List, Dict


def dump_load(employees_dict: List[Dict])->None:
    """
    Serialize and Deserialize the file
    """

    # Serialization using JSON
    with open("employees.json","w") as file:
        json.dump(employees_dict, file)
        print("Serializing successful: employees.json")


    # Deserialization using JSON
    with open("employees.json","r") as file:
        dat= json.load(file)
        print("Deserializing successful: employees.json")


#
employees=[{"name":"raj","rank":"manager","age":23},
           {"name": "vishal","rank": "senior","age":25},
           {"name": "rahi","rank": "junior","age":18}
]

dump_load(employees)