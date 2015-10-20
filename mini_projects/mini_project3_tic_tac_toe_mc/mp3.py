"""
Monte Carlo Tic-Tac-Toe Player
http://www.codeskulptor.org/#user40_X4x9UVRpVk_49.py
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def mc_trial(board, player):
    '''
    Function that make monte-carlo trials
    '''
    
    while not board.check_win():
        empty_squares = board.get_empty_squares()
        pick = empty_squares[random.randrange(len(empty_squares))]
        board.move(pick[0],pick[1],player)
        if not board.check_win():
            player = provided.switch_player(player)
    
def mc_update_scores(scores, board, player):
    '''
    Updating the score board
    '''

    if board.check_win() == provided.DRAW:
        pass
    else:   
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row,col) == provided.EMPTY:
                    scores[row][col] += 0
                elif player == board.check_win():
                    if board.square(row,col)==player:
                        scores[row][col] += SCORE_CURRENT
                    else:
                        scores[row][col] -= SCORE_OTHER
                else:
                    if board.square(row,col)==player:
                        scores[row][col] -= SCORE_CURRENT
                    else:
                        scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    '''
    Get the best move
    '''
    print scores
    empty_squares = board.get_empty_squares()
    print 'empty square:', empty_squares
    if not len(empty_squares):
             return

    max_score_val = max([scores[row][col] for row,col in empty_squares])
    max_score_squares = [(row,col) for col in range(board.get_dim()) for row in range(board.get_dim()) if scores[row][col] == max_score_val]
    print 'max value:', max_score_val
    print 'max value squares:', max_score_squares
    print 'empty square:',empty_squares
    empty_max = list(set(max_score_squares).intersection(empty_squares))
    print 'empty_max', empty_max
    best_move = random.choice(empty_max)
    return best_move
    
        

def mc_move(board, player, trials):
    '''
    Number of monte-carlo move trials
    '''
    my_scores = [[0 for dummy in range(board.get_dim())] 
                 for dummy in range(board.get_dim())]
    
    for dummy_numt in range(trials):
        current_board=board.clone()
        mc_trial(current_board,player)
        mc_update_scores(my_scores, current_board, player)
    return get_best_move(board, my_scores)
        
        
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.


#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

