# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

# bin() 2진수로 변환하는 파이썬 기능

def solution(n):
    answer = 0
    a = bin(n)
    b = a.count('1')
    while 1:
        n += 1
        c = bin(n)
        d = c.count('1')
        if b == d:
            return n
    return answer
