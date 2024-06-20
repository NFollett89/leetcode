# https://leetcode.com/problems/random-pick-with-weight/

import random

class Solution:
    # Intuition: Think of a cyclist climbing a hill, where the weights are the grade/steepness of the hill
    # over a standard distance/index. Positive integers mean the hill only goes up, never down or flat, but
    # with varying degrees. A prefix sum array lets us find the amount of "work" done over time/indices,
    # tells us the inclusive-max value for our random integer generation, and allow a binary search to find the index
    # which had done that amount of "work".

    def __init__(self, w: List[int]):
        self.w_sums = []
        rand_max = 0
        for weight in w:
            rand_max += weight
            self.w_sums.append(rand_max)
        self.rand_max = rand_max

    def pickIndex(self) -> int:
        w_choice = random.uniform(0, self.rand_max)
        left = 0
        right = len(self.w_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.w_sums[mid] < w_choice:
                left = mid + 1
            else:
                right = mid
        return left
