"""
Leetcode Q2131 - Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import defaultdict
        word_counts = defaultdict(int)

        for word in words:
            word_counts[word] += 1

        double_letter_word_remaining = False
        length = 0
        for word in word_counts:
            if word[0] == word[1]:
                while word_counts[word] > 1:
                    length += 4
                    word_counts[word] -= 2
                if word_counts[word] == 1:
                    double_letter_word_remaining = True

            else:
                opposite = f"{word[1]}{word[0]}"
                if opposite in word_counts:
                    while word_counts[word] > 0 and word_counts[opposite] > 0:
                        length += 4
                        word_counts[word] -= 1
                        word_counts[opposite] -= 1

        return length + 2 if double_letter_word_remaining else length
