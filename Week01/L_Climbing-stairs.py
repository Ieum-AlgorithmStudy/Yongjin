# https://leetcode.com/problems/search-insert-position/description/


# 손으로 풀어봤을때 문제 방식이 보이는 문제였습니다.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1,1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#당신은 계단을 오르고 있습니다. 정상에 도달하려면 n 단계가 필요합니다.
# 매번 1~2계단씩 오를 수 있습니다. 얼마나 많은 방법으로 정상에 오를 수 있나요?

