class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is out of the valid range
        if sum < 1 or sum > 9 * num:
            return ""
        
        result = []
        rem_sum = sum
        
        for i in range(num):
            # We want the largest possible digit for the current position (from 9 down to 0)
            # such that the remaining sum can be formed by the remaining positions (num - 1 - i) * 9
            remaining_positions = num - 1 - i
            
            # The digit can be at least (rem_sum - 9 * remaining_positions)
            # and at most 9, but not less than 0.
            # Also, if it's the very first digit (i == 0) and num > 1, 
            # it cannot be 0, but since rem_sum <= 9 * num and rem_sum >= 1, 
            # greedily choosing the max will naturally handle leading zeros correctly 
            # as long as remaining sums are respected.
            
            low = max(0, rem_sum - 9 * remaining_positions)
            high = min(9, rem_sum)
            
            # Greedily pick the largest valid digit
            chosen_digit = high
            while chosen_digit >= low:
                # Check if this choice leaves a valid remaining sum
                if rem_sum - chosen_digit <= 9 * remaining_positions:
                    break
                chosen_digit -= 1
            
            result.append(str(chosen_digit))
            rem_sum -= chosen_digit
            
        return "".join(result)