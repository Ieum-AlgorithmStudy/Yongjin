# https://leetcode.com/problems/valid-parentheses/submissions/?source=submission-noac

# 하나의 스택에 넣어서 조건을 걸다보니 코드가 조금 길어졌는대 조금더 단순하게 구현이 가능할 것 같습니다.

class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                a.append(i)
            
            else:
                if i == ')':
                    if len(a) != 0:
                        if a.pop() != '(':
                            return False
                    else:
                        return False
                elif i == '}':
                    if len(a) != 0:
                        if a.pop() != '{':
                            return False
                    else:
                        return False
                elif i == ']':
                    if len(a) != 0:
                        if a.pop() != '[':
                            return False
                    else:
                        return False
                
        if len(a) != 0 :
            return False
        return True           
    


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# '(', ')', '{', '}', '[' 및 ']' 문자만 포함하는 문자열 s가 주어지면 입력 문자열이 유효한지 확인합니다.
# 다음과 같은 경우 입력 문자열이 유효합니다.


# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# 열린 괄호는 동일한 유형의 괄호로 닫혀야 합니다.
# 열린 괄호는 올바른 순서로 닫혀야 합니다.
# 모든 닫는 괄호에는 동일한 유형의 해당 열린 괄호가 있습니다.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.