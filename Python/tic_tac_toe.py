# import tkinter as tk
# from tkinter import messagebox

# class TicTacToe:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tic Tac Toe")

#         self.current_player = "X"
#         self.board = [["" for _ in range(3)] for _ in range(3)]
#         self.board_buttons = [[None for _ in range(3)] for _ in range(3)]

#         self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("Arial", 14))
#         self.status_label.pack(pady=10)

#         self.grid_frame = tk.Frame(self.root)
#         self.grid_frame.pack()

#         for row in range(3):
#             for col in range(3):
#                 self.button[row][col] = tk.Button(
#                     self.grid_frame, 
#                     text="", font=("Arial", 20), 
#                     width=5, height=2,
#                     command=lambda r=row, 
#                     c=col: self.on_click(r, c)
#                     )
#                 self.button[row][col].grid(row=row, column=col,padx=5, pady=5)
#     def on_click(self, row, col):
#         if self.board[row][col] == "":
#             self.board[row][col] = self.current_player
#             self.board_buttons[row][col].config(text=self.current_player)

#             if self.check_winner():
#                 messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
#                 self.reset_game()
#             elif self.check_draw():
#                 messagebox.showinfo("Game Over", "It's a draw!")
#                 self.reset_game()
#             else:
#                 self.current_player = "O" if self.current_player == "X" else "X"
#                 self.status_label.config(text=f"Player {self.current_player}'s turn")

#     def check_winner(self):
#         for row in range(3):
#             if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
#                 return True

#         for col in range(3):
#             if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
#                 return True

#         if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
#             return True

#         if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
#             return True

#         return False
    
#     def check_draw(self):
#         for row in range(3):
#             for col in range(3):
#                 if self.board[row][col] == "":
#                     return False
#         return True
    
                
#     def reset_game(self):
#         self.current_player = "X"
#         self.board = [["" for _ in range(3)] for _ in range(3)]
#         self.status_label.config(text=f"Player {self.current_player}'s turn")

#         for row in range(3):
#             for col in range(3):
#                 self.board_buttons[row][col].config(text="")

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TicTacToe(root)
#     root.mainloop()
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self,root):
        self.root=root
        self.root.title("Tic Tac Toe")

        self.current_player="X"
        self.board=[["" for _ in range(3)] for _ in range(3)]
        self.buttons=[[None for _ in range(3)] for _ in range(3)]

        self.status_label=tk.Label(root,text="player X's Turn", font=("Arial",16))
        self.status_label.pack(pady=10)

        self.grid_frame=tk.frame(root)
        self.grid_frame.pack()

        for row in range(3):
            for col in range(3):
                self.buttons[row][col]= tk.Button(
                    self.grid_frame,
                    text="",
                    font=("Arial",24),
                    width=5,
                    height=2,
                    command=lambda r=row,c=col: self.on_click(r,c)
                )
                self.buttons[row][col].grid(row=row,column=col,padx=5,pady=5)
    
    def check_winner(self,r,c):
        p=self.current_player
        if all(self.board[r][i]==p for i in range(3)):return True
        if all(self.board[i][c]==p for i in range(3)): return True

        if r ==c and all(self.button[i][i]==p for i in range(3)):return True
        if r+c==2 and all(self.board[i][2-1]==p for i in range(3)):return True
        return False

    def is_draw(self):
        return all(self.board[row][col]!= "" for row in range(3) for col in range(3))

    
    def on_click(selfd,row,col):
        if self.board[row][col] =="":
            self.board[row][col]=self.current_player
            self.buttons[row][col]=comfig(text=self.current_player)

            if self.current_player=="X":
                self.buttons[row][col].comfig(fg="blue")
            else:
                self.buttrom[row][col].configf(fg= "red")


            if self.check_winner(row,col):
                messagebox.showinfo("Game over","Player "+self.current_player+" wins!")
                self.reset_board()

            elif self.is_draw():
                messagebox.showinfo("Game over","Draw!")
                self.reset_board()
            else:
                self.current_player= "O" if self.current_player=="X" else "X"
                self.status_config (text=" player{self.current_player}'turn ")
    def reset_board():
        self.current_player="X"
        self.status_label.config(text="player X's Turn")
        self.board=[["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="",fg="black")


if __name__ == '__main__':
    windows=tk.Tk()
    game=TicTacToe(windows)
    windows.mainLoop()