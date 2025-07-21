class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1 
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1 , right + 1]
            elif curr_sum < target :   # need to increase  value of the current sum 
                left += 1 
            else:                      # curr sum > target    need to decrease value 
                right -= 1 
        return -1 # else return -1 