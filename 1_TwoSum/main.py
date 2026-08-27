class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums={}
        for index, value in enumerate(nums):
            residue = target - value
            if residue in seen_nums:
                return seen_nums[residue], index
            seen_nums[value] = index
        return []
                    
                    
                
                    
                
        