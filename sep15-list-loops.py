# cities = ['HCMC', 'Ha Noi', 'Hai Phong', 'Da Nang', 'Nha Trang']

# show all elements
# print(cities)

    # counter       index
    # index + 1     0

# print('1.' + cities[0])
# print('2.' + cities[1])
# print('3.' + cities[2])

# cities.append('Vinh')
# cities.insert(3, 'Quy Nhon')

# print('length of the cities list:', len(cities))

# last index = length - 1

# for i in range(len(cities)):
#     print(str(i+1) + '. ' + cities[i])
    

# print(cities.index('Da Nang')) 


# for i in range(1, len(cities), 2):
#     print(str(i+1) + '. ' + cities[i])

# in chuỗi ngược
# for i in range(len(cities) - 1, -1, -1):
#     print(str(i+1) + '. ' + cities[i])


# menu = ['sushi', 'ramen', 'udon', 'sashimi']

# order = input('What do you like to order: ')

# kĩ thuật đặt cờ (flag)
# found = False

# for i in range(len(menu)):
    # print(menu[i])
    # lỗi sai phổ biến:
        # dùng else trong for để kết luận ko tìm thấy
        # ===> kết luận ko thấy SAU KHI đã tìm hết danh sách
    # if order == menu[i]:
    #     print(f'Your order of {order} is on the way')
    # else:
    #     print(f'Sorry we dont have {order}')

    # if order == menu[i]:
    #     found = True

# sử dụng flag để quyết định, NGOÀI VÒNG LẶP
# if found: 
#     print(f'Your order of {order} is on the way') 
# else:
#     print(f'Sorry we dont have {order}')


# Algorithm: thuật toán
# Linear Search

# menu.index(order) # có thể gây lỗi

# print('print sau lỗi')


# Sử dụng index để tìm 1 phần tử trong list (not recommended)
# try:
#     menu.index(order) # có thể gây lỗi
#     print(f'Your order of {order} is on the way') 
# except:
#     print(f'Sorry we dont have {order}')


HW:
games = ['lien minh', 'valorant', 'lien quan']

Chương trình cho phép user thực hiện 4 chức năng:
    1. Show tất cả các games trong list (show có counter)
        - ví dụ:
            1. lien minh
            2. valorant
            3. lien quan
    2. Thêm 1 game vào list
    3. Xoá 1 game trong list
    4. Quit chương trình
    
    
Chương trình phải dc bọc trong 1 cái while loop.

Chọn chức năng (1-4): 1
List của bạn hiện đang có 3 games:
    1. lien minh
    2. valorant
    3. lien quan

Chọn chức năng (1-4): 2
Nhập tên game mới: tốc chiến
Tốc chiến đã được thêm vào list game của bạn.

Chọn chức năng (1-4): 1
List của bạn hiện đang có 3 games:
    1. lien minh
    2. valorant
    3. lien quan
    4. tốc chiến
    
Chọn chức năng (1-4): 3
Nhập tên game để xoá: valorant
(nếu game có trong list) Valorant đã dc xoá khỏi list.

Chọn chức năng (1-4): 3
Nhập tên game để xoá: audition
(nếu game ko có trong list) Bạn ko có game audition trong list để xoá.

Chọn chức năng (1-4): 1
List của bạn hiện đang có 3 games:
    1. lien minh
    2. lien quan
    3. tốc chiến
    
Chọn chức năng (1-4): 4
Goodbye! 

- Hint: 
    1. làm từng chức năng nhỏ 1-4
    2. bọc cả chương trình trong 1 while loop