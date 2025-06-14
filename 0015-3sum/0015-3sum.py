class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicate values for i

            left, right = i + 1, n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res
