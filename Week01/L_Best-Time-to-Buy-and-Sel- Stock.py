# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_num = 0

        while right < len(prices):
            num = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_num = max(num,max_num)
            else:
                left = right

            right +=1
        return max_num 

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# 가격[i]이 i번째 날의 특정 주식 가격인 배열 가격이 제공됩니다.
# 특정 주식을 구매할 하루를 선택하고 해당 주식을 판매할 미래의 다른 날을 선택하여 수익을 극대화하고 싶습니다.
# 이 거래에서 얻을 수 있는 최대 이익을 반환합니다. 이익을 얻을 수 없으면 0을 반환합니다.
    
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# 설명: 2일차 매수(가격 = 1), 5일차 매도(가격 = 6), 이익 = 6-1 = 5.
# 2일차 매수, 1일차 매도는 매도 전 매수해야 하므로 주의하세요.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.