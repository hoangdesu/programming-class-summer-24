# Lv1:
# enter weight (kg):
# enter height (m):
    
# bmi = ...

# a ^ 2 => a ** 2


# if bmi ??: healthy |


# 1. underweight
# 2. healthy
# 3. overweight
# 4. obese

# Your BMI is 23. You are healthy

# Lv2:
#     validate

# Your BMI is 28. You are overweight
# You need to lose 20 kg to be healthy

# Your BMI is 16. You are underweight
# You need to gain 20 kg to be healthy

# # 23
# # 1m75
# # 90 -> 70 => lose 20 kg

# height 1.75
# weight 90
# bmi = 29

# bmi = 22
# height = 1.75

# bmi = w / h ^ 2

# new weight = h**2 * bmi

# 70 - 90 = -20 => LOSE 20 kg 
# 120 - 90 = 30 kg => GAIN

# year = 1995

# print('hello ' + str(year)) # String concatenation
# print(f'I was born in {float(year)} :D') # String format

    
weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))

bmi = weight / (height ** 2)

healthy_bmi = 23
healthy_weight = height**2 * healthy_bmi

print(weight, healthy_weight)

difference = healthy_weight - weight

print(difference)

if healthy_weight > weight:
    print(f'You need to GAIN {difference:.2f} kg')
elif healthy_weight < weight:
    print(f'You need to LOSE {-difference:.2f} kg')

