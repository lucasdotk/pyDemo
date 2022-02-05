from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i, ele in enumerate(nums):
            if i > 0 and nums[i-1] == ele:
                continue

            left = i + 1
            right = n - 1
            while left < right:

                # 防止重复--左边界开始于left的起始值
                if left > i + 1 and nums[left - 1] == nums[left]:
                    left += 1
                    continue
                # 防止重复--右边界
                if right + 1 < n and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                if nums[left] + nums[right] == -ele:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -ele:
                    right -= 1
                else:
                    left += 1

        return res


nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))
