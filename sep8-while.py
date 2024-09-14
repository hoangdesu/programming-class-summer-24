
# for i in range(number):
#     ...
    
    
    
# While loop: 
    
# num = 2

# while num < 10:
#     print(num)

# fav_num = int(input('Guess my favorite number: '))

# while fav_num != 102:
#     fav_num = int(input('Wrong. Guess again my favorite number: '))

# print('Correct!')

# Guess the random number
# import random

# rand_num = random.randint(0, 100)
# fav_num = int(input('Guess my favorite number: '))
# count = 1

# while fav_num != rand_num:
#     if fav_num > rand_num:
#         fav_num = int(input('Guess lower: '))
#     else:
#         fav_num = int(input('Guess higher: '))
#     count += 1

# print(f'Correct! The number is {rand_num}. You guess it in {count} times')

# Scoreboard:
#     - Phu: 5 -> 3
#     - Hieu: 7
#     - Beo: 5

# C / C++
# C#

# count = 1
# while count < 10:
#     print('inside while:', count)
    
#     # manually update the condition
#     count = count + 1

# print('outside while:', count)

# scope of a variable

# for i in range(1, 10):
#     print(i)
    
# print('outside for', i)

# name = 'outside if'
# if False:
#     name = 'inside if'
    
# print(name)
    
# 3 input:
#     start: 3
#     stop: 10
#     step: 2
    
#     3 5 7 9

# print('first line', end=" ")
# print('2nd line')



# 3 input:
#     start: 20
#     stop: 5
#     step: 3

# -> 20 17 14 11 8

# Simple calculator
# Enter a number: 1

# num = int(input('Enter a number: '))
# total = 0

# while num != 0:
#     total += num    
#     num = int(input('Enter another number: '))

# print(f'Total = {total}')

# Homework: 

# Enter a number for factorial: 5

# Factorial: 
#     Output: "5! = 5 * 4 * 3 * 2 * 1 = 120"

# while
# gom số
# gom chữ: build string

# 0! = 1

n = 5
total = 1
output = f'{n}! = '

while n >= 1:
    # print(n)
    total = total * n
    output += str(n)
    
    if n == 1:
        output += ' = '
    else:
        output += ' x '
        
    n -= 1
    
output += str(total)
print(output)
    
# 5! = 5 x 4 x 3 x 2 x 1 = 120