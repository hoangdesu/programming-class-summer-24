# List:
#     - collection of something similar
#     - []
#     - index starts 0 
    
favorite_food = ['phở', 'cơm tấm', 'bún riêu']

print(favorite_food)
    
# Access by index
print(favorite_food[2])

# print(favorite_food[3]) # IndexError: list index out of range

# Re-assign: gán lại giá trị mới
favorite_food[2] = 'bún đậu mắm tôm'


# Add new elements (at the end of the list):
favorite_food.append('nem chua rán')
favorite_food.append('hủ tiếu')
favorite_food.append('cơm gà')


# Add new elements at the START of the list
favorite_food.insert(0, 'sầu riêng')
favorite_food.insert(0, 'bánh mì')


# Insert element at any index:
favorite_food.insert(2, 'bánh khọt')

# Xoá 1 element bằng tên => element phải tồn tại
favorite_food.remove('sầu riêng')

# Xoá bằng index:
favorite_food.pop() # xoá thằng cuối cùng

favorite_food.pop(5) # xoá thằng index số 5

print('new list:', favorite_food)

# HW:
# Cho anh 1 list với nội dung bất kì
# sử dụng các kiến thức đã học hnay:
#     - access elements
#     - re-assign elements
#     - add new elements (.append, .insert)
#     - remove elements (.remove, .pop)

print(favorite_food[2] + ' is my most favorite food')