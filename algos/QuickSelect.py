import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        return self.quickselect(0, len(nums) - 1)

    def partition(self, start, end):
        pivot_ind = random.randint(start, end)
        pivot = self.nums[pivot_ind]
        self.nums[pivot_ind], self.nums[end] = self.nums[end], self.nums[pivot_ind]

        pindex = start

        for i in range(start, end + 1):
            if self.nums[i] > pivot:
                self.nums[i], self.nums[pindex] = self.nums[pindex], self.nums[i]
                pindex += 1

        self.nums[end], self.nums[pindex] = self.nums[pindex], self.nums[end]
        return pindex

    def quickselect(self, start, end):
        k = self.k - 1
        if start <= end:

            pindex = self.partition(start, end)
            if pindex > k:
                return self.quickselect(start, pindex - 1)
            elif pindex < k:
                return self.quickselect(pindex + 1, end)
            else:
                return self.nums[k]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=3))