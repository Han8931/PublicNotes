import pdb

class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            newRow = []
            for idx in range(rowIndex+1):
                if idx==0 or idx==rowIndex:
                    r_val = 1
                else:
                    r_val = self.getRow(rowIndex-1)[idx-1]+self.getRow(rowIndex-1)[idx]
                newRow.append(r_val)
            return newRow

    def getRow2(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

solution = Solution()
row = solution.getRow(10)
print(row)

