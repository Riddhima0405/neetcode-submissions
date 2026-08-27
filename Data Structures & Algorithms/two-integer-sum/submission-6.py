class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        complement = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in complement:
                return [complement[needed], i]
        

            complement[nums[i]]=i