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


The solution involved breaking down the problem and seeing that the ans array was the repetition of the nums. Hence the first attempt involved iterating through the nums array and appending to the ans array twice. Although the solution was successfull, there was room for improvement. The next solution attempted in optimising the code and it involved using the built in operator (+) and simply added the two lists and assigned the answer to the ans array without creating an empty ans array beforehand (as in the first solution).

Space & Time Complextiy:
 - First Solution: O(n) , O(n)
 - Second Solution: O(n) , O(n)
