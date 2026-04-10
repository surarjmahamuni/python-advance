# Program: write a program to accept student name and address as input and creates dictionary

def add_student_records(number):
    """
    Add student record as key:value pair
    Args:number
    Return:student_record
    """

    student_record={}

    # Create record for given number of students
    for num in range(number):
        name=input("Enter student name: ")
        marks=int(input("Enter marks: "))
        student_record[name]=marks

    print("Records added successfully")

    return student_record

def display_student_records(student_record):
    for name,marks in student_record.items():
        print("{} has {} marks".format(name,marks))

# User input
number=int(input("Enter how many numbers student: "))

# Add student data
student_records=add_student_records(number)

# Display Records
display_student_records(student_records)