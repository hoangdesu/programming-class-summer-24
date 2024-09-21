game_list = ['lien minh', 'valorant', 'lien quan', 'tốc chiến']

print('''Commands:
1. Show tất cả các games trong library (show có counter)
2. Thêm 1 game vào library
3. Xoá 1 game trong library
4. Sửa tên 1 game trong library
5. Quit chương trình''')

while True:
    command = input('\nEnter a command (1-5): ')
    
    # print all games in the library
    if command == '1':
        print(f'You have {len(game_list)} games in your library:')
        for i in range(len(game_list)):
            print(f'\t{i+1}. {game_list[i]}')
        
    # add 1 game into the library
    elif command == '2':
        new_game = input('Enter the new game: ')
        game_list.append(new_game)
        print(f'Added new game "{new_game}" to your library!')
        
    # delete 1 game from library
    elif command == '3':
        remove_game = input('Enter the game to remove from library: ')
        # game_list.remove(remove_game) # lỗi nếu game ko có
        
        exists = False 
        for i in range(len(game_list)):
            if remove_game == game_list[i]:
                exists = True # có game để xoá
        
        if exists:
            game_list.remove(remove_game)
            print(f'Removed game "{remove_game}" from your library!')
        else:
            print(f'Game "{remove_game}" is not in your library to remove.')
            
    # edit a game
    elif command == '4':
        game_number = int(input('Enter the game number to update: '))
        game_index = game_number - 1
        
        if game_index > len(game_list) - 1:
            print('Wrong game number')
        else:
            # print(game_list[game_index])
            old_name = game_list[game_index]
            new_name = input(f'Enter new name for {old_name}: ')
            game_list[game_index] = new_name
            print(f'Updated name from "{old_name}" to "{new_name}"!')

    # exit the app
    elif command == '5':
        break

    else:
        print('Wrong command. Please enter 1-5.')
        

# CRUD app:
#     - Create
#     - Read
#     - Update
#     - Delete
    
#     friend_list = [] # 5000


# HW:
# Given a list of numbers, show the largest and smallest numbers from the list
# Example: 
#     nums = [3, 2, 7, 8, 5, 4]
#     largest number = 8
#     smallest number = 2

