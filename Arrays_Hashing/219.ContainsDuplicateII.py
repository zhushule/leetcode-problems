"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Initialize an empty dictionary to store the index of each number
        num_dict = {}

        # Loop through the array with the index and the value (num)
        for idx, num in enumerate(nums):
            # If the number is not yet in the dictionary, add it with its index
            if num not in num_dict:
                num_dict[num] = idx
            # If the number is already in the dictionary (we have seen it before)
            elif num in num_dict:
                # Get the previously stored index of the number
                index = num_dict[num]
                # Check if the difference between the current index and the previous index is less than or equal to k
                if abs(index - idx) <= k:
                    return True  # If the condition is met, return True
                else:
                    # Update the dictionary with the current index of the number (since we only care about the latest occurrence)
                    num_dict[num] = idx
        
        # If no such pair is found after the loop, return False
        return False
