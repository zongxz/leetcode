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

```
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

