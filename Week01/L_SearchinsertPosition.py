# https://leetcode.com/problems/search-insert-position/submissions/

# 조금 쉽게? 풀은 문제인대 sort를 사용했을떄 시간복잡도가 어떻게 변하는지 알아봐야겠다.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums :
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        


# 다른 풀이
# 이분탐색이라는데 답을 보고 풀어 보았지만 다시 문제가 주어졌을때 생각할수 있을지..

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l



#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

# 고유한 정수의 정렬된 배열과 대상 값이 주어지면 대상이 발견되면 인덱스를 반환합니다. 그렇지 않은 경우 순서대로 삽입되었을 경우의 인덱스를 반환합니다.
#O(log n) 런타임 복잡도를 갖는 알고리즘을 작성해야 합니다.

#Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4