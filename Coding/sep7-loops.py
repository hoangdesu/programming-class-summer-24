# > Input:
# 1. Enter number: 3
# 2. Enter number: 7
# 3. Enter number: 12
# 4. Enter number: 5
# 5. Enter number: 9


# > Output:
# Total = 3 + 7 + 12 + 5 + 9 = 36
# Average = 36 / 5 = 7.2


# for i in range(9, 4, -1):
#     print(i)

# build string
output = 'Total = '
total = 0

count = int(input('How many numbers: '))
for i in range(count):
    num = int(input('Enter a number: '))
    # total = total + num
    total += num
    
    output += f'{num}'
    if i == count - 1: # last number
        output += ' = '
    else:
        output += ' + '
    
output += str(total)

print(output)
average = total / 5
print(f'Average = {average}')