# def count_vowels(s: str) -> int:
    
# "abcdexyz" -> 2


# a i u e o ->

# name = input('what is your name: ')

# # print(name[0])
# # print(name[1])

# for i in range(len(name)):
#     print(name[i])

name = input('enter your name: ')

# vowels = 2
# hoang

# phu

vowel_count = 0

vowel_group = ('a', 'i', 'u', 'e', 'o')

for i in range(len(name)):
    # print(i, name[i])
    
    # if (
    #     name[i] == 'a' or 
    #     name[i] == 'i' or 
    #     name[i] == 'u' or 
    #     name[i] == 'e' or
    #     name[i] == 'o'):
    #     vowels += 1

    if name[i] in vowel_group:
        vowel_count += 1
        
        
print(f'Your name "{name}" has {vowel_count} vowels and {consonant_count} consonants')