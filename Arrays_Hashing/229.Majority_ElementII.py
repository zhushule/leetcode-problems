"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    # If the input list is empty, return an empty list (no majority elements).
        if not nums:
            return []
        
        # Step 1: Find potential candidates for majority elements.
        # Initialize two candidate variables and their respective counts.
        # We are maintaining two potential candidates because there can be at most two elements
        # that appear more than ⌊ n/3 ⌋ times.
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        # Loop through each element in the array.
        for num in nums:
            if candidate1 == num:
                # If the current number matches candidate1, increment its count.
                count1 += 1
            elif candidate2 == num:
                # If the current number matches candidate2, increment its count.
                count2 += 1
            elif count1 == 0:
                # If count1 is 0, assign the current number as candidate1 and set count1 to 1.
                candidate1, count1 = num, 1
            elif count2 == 0:
                # If count2 is 0, assign the current number as candidate2 and set count2 to 1.
                candidate2, count2 = num, 1
            else:
                # If the current number matches neither candidate and both counts are non-zero,
                # decrement both counts (this simulates "voting out" non-majority elements).
                count1 -= 1
                count2 -= 1
        
        # Step 2: Validate the candidates to ensure they appear more than ⌊ n/3 ⌋ times.
        result = []
        count1 = count2 = 0
        
        # Count how often candidate1 and candidate2 appear in the array.
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Get the total length of the array.
        n = len(nums)
        
        # If candidate1 appears more than ⌊ n/3 ⌋ times, add it to the result.
        if count1 > n // 3:
            result.append(candidate1)
        
        # If candidate2 appears more than ⌊ n/3 ⌋ times, add it to the result.
        if count2 > n // 3:
            result.append(candidate2)
        
        # Return the result list containing all valid majority elements.
        return result
