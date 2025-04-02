# address = ''

# 5 inputs:
#     Enter your country: 'Vietnam'
#     City: HCMC
#     District: Phu Nhuan
#     Street: Truong Sa
#     House number: 1162/26

# print(address)

# Build string 
# => 1162/26 Truong Sa street, Phu Nhuan district, Ho Chi Minh city, Vietnam

address = ''

number = '1162/26'
street = 'Truong Sa'
district = 'Phu Nhuan'

address += number + ' '
address += street + ' street, '
address += district + ' district, '

print(address)