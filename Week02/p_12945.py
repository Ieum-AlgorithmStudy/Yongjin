# 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 0, 1
    
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    answer = dp[n]
    return answer