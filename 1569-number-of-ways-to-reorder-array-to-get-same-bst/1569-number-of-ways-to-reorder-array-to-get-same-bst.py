import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways_left = helper(left)
            ways_right = helper(right)
            
            # Combinations: choose len(left) elements out of (len(left) + len(right)) positions
            comb = math.comb(len(left) + len(right), len(left))
            
            return (comb * ways_left * ways_right) % MOD
            
        # The result includes the original array itself, so we subtract 1
        return (helper(nums) - 1 + MOD) % MOD