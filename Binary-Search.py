from typing import List
import math

class demo:
    def search(self, nums: List[int], target: int):
        low, high = 0, len(nums) - 1

        while(low <= high):
             mid = math.floor((low+high)//2)
             print("mid index", mid)
             if(nums[low] == target):
                return low
             if(nums[high] == target):
                return high
             if(nums[mid] == target):
                 return mid
             elif(target < nums[mid]):
                 high = mid - 1
             else: low = mid + 1
            
        return -1
