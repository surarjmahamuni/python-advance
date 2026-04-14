def calculations(first_num, second_num):
    """
    Functions performs different mathematical operations on two numbers
    Args:
     first_num: First number
     second_num: Second number
    Returns: tuple
    """

    addition = first_num + second_num
    subtraction = first_num - second_num
    multiplication = first_num * second_num
    division = first_num / second_num

    result=(addition,subtraction,multiplication,division)
    return result

t=calculations(10,20)
print(t)
