import random

def play():
    user_point = 0
    computer_point = 0
    while user_point!=3 or computer_point!=3:   
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r','p','s'])

        if user == computer:
            print('It\'s a tie')
            continue
        # r > s, s > p, p > r

        if is_win(user, computer):
            user_point+=1
            print('You scored')
            print(f'user point: {user_point}')
        else:
            computer_point+=1
            print('Computer scored')
            print(f'computer point: {computer_point}')
        
    
        if user_point==3:
            print('You won!')
            break
        elif computer_point==3:
            print('You lost!')
            break

def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

play()