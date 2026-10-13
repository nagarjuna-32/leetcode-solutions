class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square all elements
        squared = [x * x for x in nums]
        # Sort the squared values
        squared.sort()
        
        n = len(squared)
        mid = n // 2
        
        # Subtract the smaller half and add the larger half
        ans = sum(squared[mid:]) - sum(squared[:mid])
        return ans