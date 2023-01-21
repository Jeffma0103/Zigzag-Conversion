#以"PAYPALISHIRING"為例
#字串字元:PAYPALISHIRING
#應在行數:12321232123212
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            temp = list(range(numRows)) + list(range(numRows-2,0,-1))
            result = [""] * numRows
            for i,char in enumerate(s):
                result[temp[i % len(temp)]] += char
            return "".join(result)