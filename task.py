# import functools

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


# Task 10 

# nums = [-1, 2, 3, 4, -5, 6, 7, -8, 9, 0, -2, 0, 14, -6, 0]

# pos  = list(filter(lambda x : x > 0, nums))
# neg  = list(filter(lambda x : x < 0, nums))
# zero = list(filter(lambda x : x == 0, nums))

# print (f'Положительные : {pos}')
# print (f'Отрицательные : {neg}')
# print (f'Нулей в списке : {len(zero)}')


# Task 11


# nums = [-1, 2, 3, 0, 4, -5, 0, 6, 7, -8, 9, 0]

# new_nums = list(map(lambda x : -1 if x < 0 else 1 if x != 0 else 0, nums))

# print(new_nums)


# Task 12

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# def shift(steps = int(input ('Шаг сдвига : '))):
#     if steps < 0:
#          steps = abs(steps)
#          for x in range(steps):
#              nums.append(nums.pop(0))
#     else:
#          for x in range(steps):
#             nums.insert(0, nums.pop())


# shift()
# print(nums)


#Task 13


# def reverseArray(a):
#     return a [::-1]


#Task 14 

# def isBalanced(s):
#     res = []
#     brackets = { '{':'}', '(':')', '[':']' }

#     for char in s :
#         if char in ['{', '(', '['] :
#             res.append(char)
#         else:
#             if res:
#                 top = res.pop()
#                 if brackets[top] != char :
#                     return 'NO'
#             else:
#                 return "No"
#     return "NO" if res else "YES"