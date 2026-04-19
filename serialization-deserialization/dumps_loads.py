import json
from textwrap import indent
from typing import List

def dumps_loads(employees:List[dict]) -> None:
    """
    Serializing python dict and deserializing JSON string
    """

    # Serialization to JSON string
    json_string=json.dumps(employees)
    print(json_string)


    # Deserialization to python dict

    data=json.loads(json_string)
    print("Deserialization successful\n")
    print(data)



#
employees=[{"name":"raj","rank":"manager","age":23},
           {"name": "vishal","rank": "senior","age":25},
           {"name": "rahi","rank": "junior","age":18}
]
dumps_loads(employees)