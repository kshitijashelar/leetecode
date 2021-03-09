# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:57:55 2021

@author: kshit
"""

'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
'''
class Solution:
    def asteroidCollision(self, asteroids):
        finalArr =[]
        
        for x in asteroids:
            # does it collide?
            # Inside the while loop there will be a colission
            while len(finalArr) and x < 0 and finalArr[-1] > 0:
                #Both have same maghnitude so they both break
                if (finalArr[-1] + x) == 0:
                    finalArr.pop()
                    break
                
                # Incoming asteroid breaks
                elif abs(x) < finalArr[-1]:
                    break
                
                # top asteroid in stack breaks
                else:
                    finalArr.pop()
                    continue
            else:
                #appending asteroid to res
                finalArr.append(x)
                
        return finalArr
    
S = Solution()
print(S.asteroidCollision(  [10,2,-5]))