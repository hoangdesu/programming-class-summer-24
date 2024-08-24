# print(10 / 2)
# print(10 % 2) # mod (modulus) => tính phần dư

# print(10 / 3)
# print(10 % 3)

# print(1.236 % 1)

# # 2.5 hours => 2 hours + 0.5 hours

# hour = int(2.5)
# print(hour)

# minute = 2.5 % 1 * 60
# print(minute)

# Conditionals: cau dieu kien

# if condition is true:
#     action1
# else:
#     action2


# boolean: True | False

# is_raining = False

# if is_raining:
#     print('ở trong nhà')
# else:
#     print('đi ra ngoài chơi :D')

# tab: indent in ->
# shift tab: indent out <-

# elif = else if

# country = input('Where are you from: ').lower()

# if country == 'vietnam':
#     print('xin chào')
# elif country == 'japan':
#     print('konnchiwa')
# elif country == 'china':
#     print('ni hao')
# elif country == 'korea':
#     print('annyeong haseyo')
# elif country == 'france':
#     print('bonjour')
# else:
#     print('hello')



# Kết hợp các câu điều kiện

# bún đậu + mắm tôm

# bún đậu nước mắm ?

# phở + bò

# and


# bundau = True
# mamtom = True


# if bundau == True and mamtom == True:
#     print('Bun dau mam tom')

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == 'brian' and password == 'hehe':
    print('Login successfully!')
else:
    print('Login failed...')

gpa = int(input('Enter your GPA: '))

# 80-100: A
# 70-79: B
# 60-69: C
# 50-59: D
# < 50: F

    
if 80 <= gpa <= 100:
    print('You got an A!')
elif 70 <= gpa < 80:
    print('You got a B')
...

105 or -10 => wrong gpa format. Please enter a number between 0-100
