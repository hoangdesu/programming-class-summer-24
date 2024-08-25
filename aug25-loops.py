# Loops: vòng lặp

# for vs while

# for i in range(1000):
#     print(str(i) + '. hehe')

# 0 -> x-1
# for x in range(20):
#     if x % 2 == 0:
#         print(f'{x}: even number')
#     elif x % 2 == 1:  # x % 2 != 0
#         print(f'{x}: odd number')

# range(start, stop-1)
# for counter in range(9, 102):
#     print(counter)

# range(start, stop, step)
# for counter in range(10, 50, 3):
#     print(counter)

# for i in range(20, 10, -1):
#     print(i)

# i: 0 -> 10
# counter: 0 2 4 8 16 32 ...

# counter = 0
# print(counter)
# counter = counter + 2
# for i in range(11):
#     print(i, ':', counter)
#     if counter == 0:
#         counter = counter + 2
#     else:
#         counter = counter * 2


# for i in range(1.5):
#     print(i)

# start = int(input('Enter start: '))
# stop = int(input('Enter stop: '))

# for i in range(start, stop + 1):
#     print(i, end=" ")


# Exercise:
# factorial: giai thừa
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Enter a number: 5

# Factorial of 5 is 120
# 5! = 120

# number = int(input('Enter a number: '))
# factorial = 1
# for i in range(number, 0, -1):
#     # print(i)
#     factorial = factorial * i

# print(factorial)

# while user dont click on exit: 
#     run()

# while True:
#     print('=))')
    
        
# // HOMEWORK: 

1. Cho phép user nhập vào 5 số
2. Tính tổng 5 số đó
3. Tính trung bình cộng của 5 số đó

Ví dụ:
    
> Input:
1. Enter number: 3
2. Enter number: 7
3. Enter number: 12
4. Enter number: 5
5. Enter number: 9


> Output:
Total = 3 + 7 + 12 + 5 + 9 = 36
Average = 36 / 5 = 7.2


