class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_element = None
        count = 0

        for i in nums:
            if count == 0:
                max_element = i
            if i == max_element:
                count+=1
            if i != max_element:
                count -= 1
        return max_element