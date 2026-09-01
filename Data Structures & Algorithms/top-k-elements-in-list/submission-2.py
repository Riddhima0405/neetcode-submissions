class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        return [num for num, _ in freq.most_common(k)]