"""

Concatenation of Array
You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,4,1,2]

Output: [1,4,1,2,1,4,1,2]
Example 2:

Input: nums = [22,21,20,1]

Output: [22,21,20,1,22,21,20,1]
Constraints:

1 <= nums.length <= 1000.
1 <= nums[i] <= 1000


TEST CASE 1:
nums =[1,4,1,2]

TEST CASE 2:
nums =[22,21,20,1]
"""



class Solution: #ORGINAL (NO OPTIMISATION)
    def getConcatenation(self,nums): # Space = O(n), Time = O(n)
        ans = []

        for i in nums:
            ans.append(i)
        
        for i in nums:
            ans.append(i)
        
        print(ans) # added for checking, not needed
        return ans


sol = Solution()
nums1 =[1,4,1,2]
nums2 =[22,21,20,1]

ans1 = sol.getConcatenation(nums1)
ans2 = sol.getConcatenation(nums2)


class Solution2: #SECOND ATTEMPT W/ OPTIMISATION
    def getConcatenation2(self, nums): # Space = O(n), Time = O(n)
        ans = nums+nums
        print(ans) # added for checking, not needed
        return ans



sol2 = Solution2()

ans2_a = sol2.getConcatenation2(nums1)
ans2_b = sol2.getConcatenation2(nums2)