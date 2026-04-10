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

def search_student_records(student_record):
    """
    Search student record in the dictionary
    Args:
    student_record {dict}: student record
    Return:
    None
    """

    while True:

        student_name=input("Enter the student name: ")
        student_marks=student_record.get(student_name,-1)

        if student_marks==-1:
            print("Student doesnt exist in the records.")

        else:
            print(f"{student_name} marks are {student_marks}")

        option=input("Do you want to continue (yes/no)").lower()
        if option=='no':
            break


# User input
number=int(input("Enter how many numbers student: "))

# Add student data
student_records=add_student_records(number)

# Display Records
display_student_records(student_records)

# Search record
search_student_records(student_records)