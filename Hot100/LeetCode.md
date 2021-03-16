# LeetCode HOT 100

# 461 汉明距离

## 题目描述

```text
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 2^31.

```

## 思路

### 方法一：标准解法

```text
当 x，y 不等于 0 时，比较下 x，y 对 2 取余，不相等则 res + 1，然后 x，y 除以 2，进行下一次循环。
```

### 方法二：内置位计数功能

```text
大多数编程语言中，都存在各种内置计算等于 1 的位数函数。
java 的 bitCount() 函数。
```



## 代码实现

### 方法一：标准解法

```python
class Solution:
    def hammingDistance(self, x, y):
        res = 0
        if x == y:
            return 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                res += 1
            x //= 2
            y //= 2
        return res
```

### 方法二：内置位计数功能

#### python

```python
class Solution:
	def hammingDistance(self, x, y):
		return bin(x ^ y).count('1')
```

#### Java

```java
class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y); 
    }
}
```
# 104 二叉树的最大深度

## 题目描述

```text
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

```

## 思路

### 深度优先搜索

```text
左子树和右子树的最大深度 lmax 和 rmax，那么该二叉树的最大深度即为 max(lmax, rmax) + 1
```

## 代码实现

```python
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            lmax = self.maxDepth(root.left) + 1
            rmax = self.maxDepth(root.right) + 1
            return max(lmax, rmax)
```
# 136 只出现一次的数字

## 题目描述

```text
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

```

## 思路

### 方法一：哈希法

```text
不考虑空间和时间可以使用哈希法

使用哈希表存储每个数字和该数字出现的次数。遍历数组即可得到每个数字出现的次数，并更新哈希表，
最后遍历哈希表，得到只出现一次的数字。
```

### 方法二：位运算 — 异或法

```text
异或运算有以下三个性质:
1. 任何数和 00 做异或运算，结果仍然是原来的数，即 a ^ 0 = a .
2. 任何数和其自身做异或运算，结果是 0，即 a ^ a = 0 。
3. 异或运算满足交换律和结合律，即 a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b

假设数组中有 2m+1 个数，其中有 m 个数各出现两次，一个数出现一次。令 a1, a2, ... , am 为出现两次的 m 个数，
am+1 为出现一次的数。根据性质 3，数组中的全部元素的异或运算结果总是可以写成如下形式：
					(a1 ^ a1) ^ (a2 ^ a2) ^...^(am ^ am) ^ am+1
根据性质 2 和性质 1，上式可化简和计算得到如下结果：
					0 ^ 0 ^ 0 ^ ... ^ 0 ^ am+1 = am+1
因此，数组中的全部元素的异或运算结果即为数组中只出现一次的数字。
```

```
python reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
此题可写成：reduce(lambda x, y: x ^ y, nums)
```



## 代码实现

### 方法一：哈希法

```python
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
```

### 方法二：异或法

```python
class Solution:
    def singleNumber(self, nums):
        # 位运算法————异或法
        # 不需要额外的空间
        return reduce(lambda x, y: x ^ y, nums)
```

