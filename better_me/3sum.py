from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_dict = {num: i  for i, num in enumerate(nums)}
        res = []
        nums.sort()
        print(nums)
        print(hash_dict)

        length = len(nums)
        for i in range(length):
            cur = nums[i]
            for j in range(i + 1, length):
                cur_j = nums[j]
                if (0 - cur - cur_j) in hash_dict and hash_dict[(0 - cur - cur_j)] not in [i,j]:
                    res.append([cur, cur_j, (0 - cur - cur_j)])

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
