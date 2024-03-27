"""
Leetcode Q1275 - Find Winner on a Tic-Tac-Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.


Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def get_player(index):
            return 'A' if index % 2 == 0 else 'B'

        def check_horizontal(moves):
            for row in range(3):
                if [row, 0] in moves and [row, 1] in moves and [row, 2] in moves:
                    player = get_player(moves.index([row, 0]))
                    if player == get_player(moves.index([row, 1])) and player == get_player(moves.index([row, 2])):
                        return player

        def check_vertical(moves):
            for col in range(3):
                if [0, col] in moves and [1, col] in moves and [2, col] in moves:
                    player = get_player(moves.index([0, col]))
                    if player == get_player(moves.index([1, col])) and player == get_player(moves.index([2, col])):
                        return player
            return None

        def check_diagonal(moves):
            if [1, 1] in moves:
                player = get_player(moves.index([1, 1]))
                if [0, 0] in moves and player == get_player(moves.index([0, 0])):
                    if [2, 2] in moves and player == get_player(moves.index([2, 2])):
                        return player
                if [0, 2] in moves and player == get_player(moves.index([0, 2])):
                    if [2, 0] in moves and player == get_player(moves.index([2, 0])):
                        return player
            return None

        winner = check_horizontal(moves)
        if winner:
            return winner

        winner = check_vertical(moves)
        if winner:
            return winner

        winner = check_diagonal(moves)
        if winner:
            return winner

        if len(moves) < 9:
            return "Pending"
        return "Draw"
