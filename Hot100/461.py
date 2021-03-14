"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
"""


class Solution:
    def hammingDistance(self, x, y):
        res = 0
        # print(x ^ y)
        # print(bin(x ^ y))
        # if x == y:
        #     return 0
        # while x != 0 or y != 0:
        #     if x % 2 != y % 2:
        #         res += 1
        #     x //= 2
        #     y //= 2
        # return res
        xor = x ^ y
        while xor:
            if xor & 1:
                res += 1
            xor = xor >> 1
        return res


s = Solution()
print(s.hammingDistance(1, 4))
