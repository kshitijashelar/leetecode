# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:50:26 2021

@author: kshit
"""

'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]'''

class Solution:
    def findDisappearedNumbers(self, nums):
        complete = set()
        for i in range(1,len(nums)+1):
            complete.add(i)
        
        finalans = complete - set(nums)
        return finalans