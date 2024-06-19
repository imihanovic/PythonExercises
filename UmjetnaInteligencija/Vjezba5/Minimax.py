from Stanje import Stanje

def perft(game: Stanje):
    global cnt_nodes
    cnt_nodes += 1
    if game.game_over() != False:
        return
    actions = game.all_actions()
    for a in actions:
        game.do_action(a)
        perft(game)
        game.undo_action(a)

def minimax(game):
    global cnt_nodes
    cnt_nodes += 1
    
    if game.game_over() == game.P1:
        return 100, 0  
    elif game.game_over() == game.P2:
        return -100, 0  
        
    if game.turn == game.P1:
        maxi, num = -1000, 0
        for number in game.all_actions():
            game.do_action(number)
            vmax = minimax(game)[0]
            game.undo_action(number)
            if vmax > maxi:
                maxi, num = vmax, number
        return maxi, num
    else:
        mini, num = 1000, 0
        for number in game.all_actions():
            game.do_action(number)
            vmin = minimax(game)[0]
            game.undo_action(number)
            if vmin < mini:
                mini, num = vmin, number
        return mini, num

def alphabeta(game, alpha, beta, d):
    global cnt_nodes
    cnt_nodes += 1
    
    if game.game_over() == game.P1:
        return 1, None
    elif game.game_over() == game.P2:
        return -1, None 
    if d == 0:
        return 0, None
    
    actions = game.all_actions()
    if game.turn == game.P1:
        best = None
        for a in actions:
            game.do_action(a)
            v, _ = alphabeta(game, alpha, beta, d-1)
            game.undo_action(a)
            if v > alpha:
                alpha = v
                best = a
            if alpha >= beta:
                return alpha, None
        return alpha, best
    else:
        best = None
        for a in actions:
            game.do_action(a)
            v, _ = alphabeta(game, alpha, beta, d-1)
            game.undo_action(a)
            if v < beta:
                beta = v
                best = a
            if alpha >= beta:
                return beta, None
        return beta, best
    
    
if __name__ == "__main__" :
    cnt_nodes = 0    
    game = Stanje()
    perft(game)
    print("Nodes: ", cnt_nodes)
    cnt_nodes = 0
    v, count = alphabeta(game, -1000, 1000, 100)
    print("Nodes - alphabeta:", cnt_nodes)
    while game.game_over() == False:
        print('*'*50)
        print("Current num of sticks: ", str(game.sticks))
        print('*'*50)
        print()
        if game.turn == game.P1:
            choice = int(input("How much sticks do you want to raise (1,2)?: ")) 
            while choice not in [1,2]:
                choice = int(input("How much sticks do you want to raise (1,2)?: ")) 
        else:
            v, choice = minimax(game)
            print("Bot raised:", choice)
        game.do_action(choice)
    print(game)