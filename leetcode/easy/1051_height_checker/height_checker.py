from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(list(filter(lambda x: x[0] != x[1], zip(heights, sorted(heights)))))
