# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# Counter는 딕셔너리로 갯수를 사용하는 방식과 동일한 파이썬 함수이다.


from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum = 0
    tan = Counter(tangerine).most_common()
    
    for t in tan:
        sum += t[1]
        answer += 1
        if sum >= k:
            return answer
    
    return answer