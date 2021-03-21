# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:37:21 2021

@author: kshit
"""
'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''

class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for s in stones:
            if s in jewels:
                count = count+1
        return count
    


S = Solution()
print(S.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))