from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    a = 0
    b = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j] == target):
                a = i
                b = j

    return [a,b]

#print(twoSum([2,7,11,15],9))
#print(twoSum([3,2,4],6))
#print(twoSum([3,3],6))