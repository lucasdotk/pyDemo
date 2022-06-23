from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        r_num = 1

        for i in range(0, len(nums) - 1):
            answer.append(nums[i] * answer[i])

        for i in range(len(nums) - 2, -1, -1):
            r_num = nums[i + 1] * r_num
            answer[i] = r_num * answer[i]

        return answer


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))

for i in range(2, 0, -1):
    print(i)
