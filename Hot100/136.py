"""
136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

"""
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        # 哈希法
        # 使用字典存储每个字符出现的次数，遍历字典返回出现次数为 1 的字符
        # 此方法会借用额外的空间
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for k, v in res.items():
            if v == 1:
                return k
        # 位运算法————异或法
        # 不需要额外的空间
        # return reduce(lambda x, y: x ^ y, nums)



s = Solution()
print(s.singleNumber([1, 5, 5, 1, 2, 2, 6]))
