class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store original indices since the list is not sorted
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()

        i = 0
        j = len(indexed_nums) - 1

        while i < j:
            current = indexed_nums[i][0] + indexed_nums[j][0]

            if current == target:
                indices = [indexed_nums[i][1], indexed_nums[j][1]]
                indices.sort()
                return indices
            elif current < target:
                i += 1
            else:
                j -= 1