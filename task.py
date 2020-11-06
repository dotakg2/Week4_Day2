import functools

# Task 2

# nums = [1,2,3]
# print(sum(nums))



# Task 1 

# nums = [1,2,3,4,5,6,7,8,9]

# squares = list(map(lambda x:x ** 2,nums))
# print(squares)




# Task 5 

# nums = [1, -2 ,3 , 0, -1]
# otris = list(filter(lambda x : x < 0,nums))
# print(otris)


# Task 6

# nums = [1,2,3,0,-1]
# iris = list(filter(lambda x:x % 2 == 0,nums))
# print(iris)


# Task 7
 
# name = ["hello", "world","incapsulation","inheritance"]
# new = list(map(lambda name:f"your name is {name}",filter(lambda x:len(x)> 6, name)))
# print(new)



#Task 8

# items = [1,2,3,4]
# sum = functools.reduce(lambda x,y:x+y,items)
# print(sum)


#Task 3

# nums = [1,2,3,0,-1]
# if any (num > 0 for num in nums):
#     print(True)
# else:
#     print(False)


# Task 9 

# list1 = [1,2,3,4,5,6,7,8,9]
# even_count , odd_count = 0, 0
# for num in list1:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers in the list: ", even_count) 
# print("Odd numbers in the list: ", odd_count) 


# Task 4

# nums = [1,2,3,0,-1]
# if any (num < 0 for num in nums):
#     print(True)
# else:
#     print(False)


