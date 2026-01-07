# Problem: Asteroid Collision
# LeetCode URL: https://leetcode.com/problems/asteroid-collision/description/
# Description: We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# challenge

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:      
                    stack.pop()
                    continue
                elif stack[-1] == -a:   
                    stack.pop()
                break                   
            else:
                stack.append(a)

        return stack
