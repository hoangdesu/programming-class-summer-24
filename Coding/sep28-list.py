# HW:
# Given a list of numbers, find the largest and smallest numbers from the list
# Example: 
#     nums = [3, 2, 7, 8, 5, 4]
#     largest number = 8
#     smallest number = 2


# for i in range(len(nums)):
    

# list of integers
# nums = [3, 2, 7, 8, 9, 10, 12, 11, 5, 4]

# # tạm thời gọi số đầu là số lớn nhất 
# largest = nums[0]
# smallest = nums[0]

# for i in range(len(nums)):
#     # print(nums[i])
    
#     # kiểm tra nếu số hiện tại còn lớn hơn số tạm thời
#     if nums[i] > largest:
#         largest = nums[i]  # gán số mới hơn vào largest
        
#     if nums[i] < smallest:
#         smallest = nums[i]

# print('largest number =', largest)
# print('smallest number =', smallest)



# Nested loops

# 60 s = 1 min
# 60 min = 1 hour
# 24 hour = 1 day

# for i in range(1, 6):
#     for j in range(7, 11):
#         print(f'i = {i} | j = {j}')


# lines = int(input('How many lines to print: '))
# shape = input('What shape: ')

# for line in range(1, lines + 1):
#     for i in range(line):
#         print(shape, end="")
#     print()
        
        
# doi anh xiu
        
# *
# **
# ***
# ****
# *****

# lines = 5
#                 line    star    space
# #     *         1       1       4
# #    ***        2       3       3
# #   *****       3       5       2
# #  *******      4       7       1
# # *********     5       9       0


lines = int(input('How many lines to print: '))
shape = input('What shape: ')
# shape = '*'

space = lines - 1

for line in range(1, lines + 1):
    for i in range(space):
        print(' ', end="")
    
    for i in range(1, line * 2):
        print(shape, end="")
        
    print()
    space -= 1
        
        