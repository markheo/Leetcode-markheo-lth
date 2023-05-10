class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        w = len(matrix[0])
        h = len(matrix)

        top, bottom, left, right = 0, h-1, 0, w-1
        if matrix == None:
            return []
        while top<=bottom and left<=right:
            #right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1

            #down
            for j in range(top, bottom+1):
                ans.append(matrix[j][right])
            right -= 1

            #left
            if top<=bottom:
                for k in range(right, left-1, -1):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            #up
            if left<=right:
                for l in range(bottom, top-1, -1):
                    ans.append(matrix[l][left])
                left += 1
        return ans