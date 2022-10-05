import emoji

board = list(range(1,10))

def draw_board(board):
    print ("-" * 15)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 15)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + emoji.emojize(":white_question_mark:"))
        try:
            player_answer = int(player_answer)
        except:
            print(emoji.emojize('Некорректный ввод.:warning: Вы уверены, что ввели число?'))
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print (emoji.emojize("Эта клеточка уже занята :warning:"))
        else:
            print (emoji.emojize("Некорректный ввод.:warning: Введите число от 1 до 9 чтобы походить."))

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(emoji.emojize(":flamingo:"))
        else:
            take_input(emoji.emojize(":dove:"))
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, emoji.emojize("выиграл! :trophy:"))
                win = True
                break
        if counter == 9:
            print (emoji.emojize("Ничья!:handshake:"))
            break
    draw_board(board)

main(board)
