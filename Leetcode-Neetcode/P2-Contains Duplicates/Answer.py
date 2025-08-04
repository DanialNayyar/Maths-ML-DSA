class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = set()
        
        for i in nums:
            if i in nums_seen:
                return True
            else:
                nums_seen.add(i)
        return False




#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
