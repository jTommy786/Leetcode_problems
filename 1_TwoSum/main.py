class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        found = False

        for i in range(len(nums)):
            sum = 0
            for j in range(len(nums)):
                print(nums.index(nums[i]))
                print(nums.index(nums[j]))
                if i != j:
                    sum = nums[i]+nums[j]
                    print("In")
                    if target == sum and found!=True:
                        found=True
                        positions = [i,j]

                        print("Found in: " + str(positions))
                        return positions
                    
                    
                
                    
                
        