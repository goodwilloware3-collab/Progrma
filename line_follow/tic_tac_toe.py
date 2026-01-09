import tkinter as tk
root=tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
board=[""]*9
buttons=[]   
game_active=True

def check_win_sim(board_state,player):
    winning_combinations=[(0,1,2),(3,4,5),(6,7,8),
                          (0,3,6),(1,4,7),(2,5,8),
                          (0,4,8),(2,4,6)]
    for a,b,c in winning_combinations:
        if board_state[a]==board_state[b]==board_state[c]==player:
            return True
    return False
def minimax(board_state,depth,is_maximizing):
    if check_win_sim(board_state,"O"):
        return 1
    if check_win_sim(board_state,"X"):
        return -1
    if "" not in board_state:
        return 0
    if is_maximizing:
        best_score=-float('inf')
        for i in range(9):
            if board_state[i]=="":
                board_state[i]="O"
                score=minimax(board_state,depth+1,False)
                board_state[i]=""
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=float('inf')
        for i in range(9):
            if board_state[i]=="":
                board_state[i]="X"
                score=minimax(board_state,depth+1,True)
                board_state[i]=""
                best_score=min(score,best_score)
        return best_score













root.mainloop()