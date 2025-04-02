# - Variables: biến
# - Arithmethic: toán học (math)
# - Loops: for + while
# - Conditionals: điều kiện: if-elif-else
# - Functions: hàm
# - Data types: kiểu dữ liệu
#     - numbers: int, float, double,...
#     - boolean: True / False
#     - char: character: 1 chữ cái e.g. 'B' + 'e' +' o', 'u' + 'P' + 'h'
#     - string: array of characters
#     [   
#         - list: 1 nhóm 
#         - dictionary: key-value pairs
#     ]
#     - null
    
    
#     (key)       (value)
#     country     capital
# {
#     vn:         Ha Noi
#     jp:         Tokyo
#     kr:         Seoul
#     ...
# }


# int a;
# print(a)

# a = 1
    
    


# - input 3 cạnh của 1 tam giác
# - cho biết tam giác đó có vuông hay ko
# - hint: dùng định lý pythagoras

import math

a = float(input('Nhập cạnh a: '))
b = float(input('Nhập cạnh b: '))
c = float(input('Nhập cạnh c: '))

# tìm cạnh huyền (cạnh lớn nhất trong a, b, c)
hypotenuse = a
side1 = b
side2 = c

if b > hypotenuse:
    hypotenuse = b
    side1 = a
    side2 = c
if c > hypotenuse:
    hypotenuse = c
    side1 = a
    side2 = b
    
# print(hypotenuse)
# print(side1)
# print(side2)

# side1^2 + side2^2

right_side = math.sqrt(side1**2 + math.pow(side2, 2))

if hypotenuse == right_side:
    print('Đây là tam giác vuông!')
else:
    print('Đây KHÔNG PHẢI là tam giác vuông :(')
    
    

HW:
    - nhập vào đường kính (circumstance) hình tròn
    - tính chu vi & diện tích hình tròn
    
    

Prime number: số nguyên tố
-> chỉ có thể chia hết cho 1 và chính nó
vd: 7, 2, 11, 13

Nhập vào 1 số: 17
17 là số nguyên tố

Nhập vào 1 số: 18
18 không phải là số nguyên tố

Hint: sử dụng modulus (%) để tính phần dư

7
1 & 7
[2 3 4 5 6] 

=> kiểm tra tất cả các số trong khoảng giữa