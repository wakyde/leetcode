class Solution:
    def twoSum(self, arr, target):
        _dict = {}
        for i, m in enumerate(arr):
            if _dict.get(target - m) is not None:
                return [i, _dict[target -m]]
            _dict[m] = i


s = Solution()
arr = [3, 3]
print(s.twoSum(arr, 6))
