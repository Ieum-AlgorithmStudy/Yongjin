# Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

# 문제가 쉬워서 생각 나는대로 만들었지만 시간초과 위험이 있어보임
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        a = len(nums)
        b = nums.count(0)
        for i in range(a):
            if nums[i] != 0:
                pass
            else:
                nums.append(0)
                
        for i in range(b):
            nums.remove(0)
        """
        Do not return anything, modify nums in-place instead.
        """


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# 정수 배열 nums가 주어지면 0이 아닌 요소의 상대적 순서를 유지하면서 모든 0을 끝으로 이동합니다.
# 배열의 복사본을 만들지 않고 이 작업을 내부에서 수행해야 합니다.

# Follow up: Could you minimize the total number of operations done?
# 후속 조치: 수행되는 총 작업 수를 최소화할 수 있습니까?