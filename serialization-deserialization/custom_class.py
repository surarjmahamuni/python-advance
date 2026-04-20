import json

class Employee:

    def __init__(self,ename,eno,erank,esalary):
        self.ename = ename
        self.eno = eno
        self.erank = erank
        self.esalary = esalary


def custom_object_serialization(employee):
    """To Serialize and Deserialize Employee object to and from JSON file/string"""

    # custom object serialization to JSON string
    json_string=json.dumps(employee)
    print(f"Printing employee object: {employee}")
    print(f"Printing json_string: {json_string}")

    # custom object serialization to json file
    with open("custom_employees.json","w") as file:
        json.dump(employee,file,indent=4)


def custom_object_deserialization():
    """To Deserialize Employee object to and from JSON file/string"""

    # Deserializing JSON string to custom object
    with open("custom_employees.json","r") as file:
        data=json.load(file)
        employee={Employee(data['ename'],data['eno'],data['erank'],data["esalary"])}

        print(type(employee))






empl=Employee("suraj",101,"senior","10000")
empl_dict=empl.__dict__
custom_object_serialization(empl_dict)

custom_object_deserialization()
