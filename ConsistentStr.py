# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:37:42 2021

@author: kshit
"""

'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words):
        count = 0
        for word in words:
            flag = True
            for element in word:
                if element not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count