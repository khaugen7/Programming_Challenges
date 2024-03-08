"""
Leetcode Q498 - Diagonal Traverse

Given an m x n Matrix mat, return an array of all the elements of the array in a diagonal order.

 
Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        forward, down = 1, -1
        row, col = 0, 0
        
        result = []
        while len(result) < len(mat) * len(mat[0]):
            result.append(mat[row][col])
            if down == -1 and (row == 0 or col == len(mat[0]) - 1):
                if col != len(mat[0]) - 1:
                    col += forward
                else:
                    row += -1 * down
                down *= -1
                forward *= -1
            elif down == 1 and (col == 0 or row == len(mat) - 1):
                if row != len(mat) - 1:
                    row += down
                else:
                    col += -1 * forward
                down *= -1
                forward *= -1
            else:
                row += down
                col += forward
            
        return result
