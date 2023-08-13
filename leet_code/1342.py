# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

"""
"""
2 ways to do it.
1. by setting the steps variable outside and increase the count.
2. by passing the variable in parameter. (more pure recursive Implmentation)

"""
class Solution:
    steps = 0
    def numberOfSteps(self, num: int) -> int:
        #self.steps1(num)
       # print(self.steps)
        print(self.steps2(num,0))

    def steps1(self, num):
        if num == 0:
            return num
        if num % 2 == 0:
            self.steps += 1
            self.steps1(num/2)
        else:
            self.steps += 1
            self.steps1(num-1)

    def steps2(self, num, steps):
        if num == 0:
            return num, steps
        if num %2 == 0:
            return self.steps2(num//2,steps+1)
        else:
            return self.steps2(num-1,steps+1)
        
obj = Solution()
obj.numberOfSteps(123)