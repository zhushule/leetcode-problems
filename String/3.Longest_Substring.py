"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str    # The input string 's'.
        :rtype: int     # The function returns an integer, which is the length of the longest substring without repeating characters.
        """
        # Initialize an empty set to store unique characters in the current window
        char_set = set()

        # Initialize the left pointer to 0. This marks the start of the sliding window.
        left = 0

        # Initialize max_length to keep track of the maximum length of substring without repeating characters.
        max_length = 0

        # Iterate over the string with 'right' pointer
        for right in range(len(s)):
            # If the character at the 'right' pointer is already in the set,
            # it means there is a repeating character, so we need to move the 'left' pointer.
            # We remove characters starting from 'left' until there are no repeats.
            while s[right] in char_set:
                # Remove the character at 'left' from the set and move 'left' to the right.
                char_set.remove(s[left])
                left += 1  # Shrink the window from the left side

            # Add the new character at 'right' to the set (this character is now part of the current window).
            char_set.add(s[right])

            # Calculate the length of the current window: (right - left + 1)
            # Update max_length if this window is longer than the previous max.
            max_length = max(max_length, right - left + 1)
            # Update max_length: max_length = max(1, 2) = 2

        # After the loop, return the maximum length of substring without repeating characters.
        return max_length

