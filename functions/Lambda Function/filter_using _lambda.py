
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def filter_func(user_list):
   even_list=list(filter(is_even,user_list))
   return even_list

user_list=[1,2,3,4,5,6,7,8,9,10]

# Method 1: without using lambda function
even_list=filter_func(user_list)
print(even_list)


# Method 2: using lambda function

user_list=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda x:x%2==0,user_list))
print(even_list)
