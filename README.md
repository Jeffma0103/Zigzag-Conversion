# Zigzag-Conversion (medium)
Solution of Zigzag Conversion

## 題目 https://leetcode.com/problems/zigzag-conversion/description/

給定一個字串 s 及指定行數 numRows, 將字串 s 轉為 numRows 行的 Z 字型, 並輸出結果。

**ex:** <br> 

Input: <br> 
s = "PAYPALISHIRING" , numRows = 3 <br>

Output: <br>
"PAHNAPLSIIGYIR" <br>

P &nbsp;&nbsp;&nbsp; A &nbsp;&nbsp;&nbsp; H &nbsp;&nbsp;&nbsp; N <br>
A &nbsp; P &nbsp; L &nbsp; S &nbsp; I &nbsp; I &nbsp; G  <br>
Y &nbsp;&nbsp;&nbsp; I &nbsp;&nbsp;&nbsp; R <br>



## Workaround &nbsp; 1

**想法** <br> 
give a s = "PAYPALISHIRING" , numRows = 4 <br>
written in a zigzag pattern is "PINALSIGYAHRPI" <br>

<img width="103" alt="截圖 2024-05-14 下午8 47 11" src="https://github.com/Jeffma0103/Zigzag-Conversion/assets/92356670/ea601b48-6376-4c5b-a2ff-b2561efc19fc">


可以發現 : <br>
s &nbsp; 依照以下排序來進行改寫為 &nbsp; zigzag pattern <br>
012321 | 012321 | 01 <br>

| 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|
|PIN|ALSIG|YAHR|PI|

再依照 "0" + "1" + "2" + "3" 的方式即可得到轉換後的字串
