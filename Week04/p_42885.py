# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) == 1:
            answer += 1
            break
    
        elif people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            answer += 1
            people.pop()
    
    return answer