
## main.py
main.py中示例了一个比较丑陋的思路（在没想到好的解题思路之前的丑陋的办法）。
1. 将负数、零、正数分成三堆。
2. 如果有零，从负数中选一个，从正数中选一个。
3. 从正数中选一个，从负数中选两个。
4. 从正数中选两个，从负数中选一个。

写完觉得自己好丑。

## main2.py
main2.py参考了 [yuzhoujr](https://leetcode.com/problems/3sum/discuss/147561/Python-tm)的做法
1. 对数组进行排序
2. 循环列表，i from 0 to len - 2
3. 因为是进行排序过的数组，对i 后面的数组进行区间压缩 left = i + 1, right = len - 1
4. 根据 nums[i] + nums[left] + nums[right] 的结果确定区间压缩的方向
