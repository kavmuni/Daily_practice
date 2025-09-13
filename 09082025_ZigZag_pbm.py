# https://leetcode.com/problems/zigzag-conversion/solutions/6753917/clean-code-explanation-with-images-steps-java-c-python/
import numpy as np
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = [[] for _ in range(numRows)]

        i = 0
        n = len(s)

        while i < n:
            #print(i, n)
            for down in range(numRows):
                if i < n:
                    mat[down].append(s[i])
                    i += 1
            print(mat)

            for up in range(numRows - 2, 0, -1): # start, stop, step
                if i < n:
                    mat[up].append(s[i])
                    i += 1
            print(mat)


        #print(mat)

        ans = ""
        for row in mat:
            ans += ''.join(row)
        #print(ans)
        return ans

zigzak =  Solution()
zigzak.convert("PAYPALISHIRING", 3)
