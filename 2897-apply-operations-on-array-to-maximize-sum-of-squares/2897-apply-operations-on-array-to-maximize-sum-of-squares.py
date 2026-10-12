class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        # Count the frequency of each bit set across all numbers
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        
        # Build k numbers by greedily placing bits from highest to lowest position
        new_nums = [0] * k
        for i in range(k):
            current_val = 0
            for j in range(30):
                if bit_counts[j] > 0:
                    current_val |= (1 << j)
                    bit_counts[j] -= 1
            new_nums[i] = current_val
            
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for x in new_nums:
            total_sum = (total_sum + x * x) % MOD
            
        return total_sum