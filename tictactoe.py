import numpy as np
from time import sleep


class TicTacToe :

    def __init__(self) :

        self.state = np.append(np.ones(9).reshape(-1,1), np.zeros((9, 2)), axis = 1)
        self.available = [0,1,2,3,4,5,6,7,8]
        self.players = [1, 2]
        np.random.shuffle(self.players)
        self.result = np.zeros((3, 1))
        self.msg = 'Nothing yet ... '

#            0  |  1  |  2
#          -----------------             [VOID  ( ),      [TIE   ( ),
#            3  |  4  |  5              PLAYER1 (X),     PLAYER1 (X),
#          -----------------            PLAYER2 (O)]     PLAYER" (O)]
#            6  |  7  |  8


    def showBoard(self) :
        boardState = [{0: '', 1: 'X', 2: 'O'}.get(x) for x in np.argmax(self.state, axis = 1)]
        board = f'  {boardState[0]}  |  {boardState[1]}  |  {boardState[2]}  \n' + 17*'_' + '\n' + f'  {boardState[3]}  |  {boardState[4]}  |  {boardState[5]}  \n' + 17*'_' + '\n' + f'  {boardState[6]}  |  {boardState[7]}  |  {boardState[8]}'
        print('\n'); print(board); print('\n')
        print(self.state)

    def updateState(self, chosen, step) :

        self.state[self.available[chosen], self.players[step % 2]] = 1.0
        self.state[self.available[chosen], 0] = 0.0
        self.available.pop(chosen)

    def checkDone(self, step) :

        cond = False
        for player in self.players :

            for i in range(3):
                cond = cond or (self.state[3*i,player] == self.state[3*i+1,player] == self.state[3*i+2,player] == 1.0) # Check rows
                cond = cond or (self.state[i,player] == self.state[i+3,player] == self.state[i+6,player] == 1.0)       # Check columns
            cond = cond or (self.state[0,player] == self.state[4,player] == self.state[8,player] == 1.0)
            cond = cond or (self.state[2,player] == self.state[4,player] == self.state[6,player] == 1.0)  
            
            if cond :
                self.winner = player
                self.msg = f'PLAYER {player} WINS !\n'
                break

        if cond:
            done = True
            self.result[self.winner] = 1.0
        elif step == 8:
            done = True
            self.result[0] = 1.0
            self.msg = 'TIE ...\n'
        else:
            done = False

        return done


    def play(self, show = True) :

        for step in range(9) :

             # Random choices
            chosen = np.random.randint(0, len(self.available))

            self.updateState(chosen, step)
            done = self.checkDone(step)

            if show :
                _ = self.showBoard()

            if done:
                if show :
                    print(self.result)
                break


if __name__ == '__main__' :

    game = TicTacToe()
    game.play()