# Case 1: map() function

user_list=[1,2,3,4,5,6,7,8,9,10]

sqr_list=list(map(lambda num:num**2,user_list))
print(sqr_list)


# Case 2: map() function using multiple sequences
user_list1=[1,2,3,4,5,6,]
user_list2=[10,20,30]

mul_list=list(map(lambda num1,num2:num1*num2,user_list1,user_list2))
print(mul_list)