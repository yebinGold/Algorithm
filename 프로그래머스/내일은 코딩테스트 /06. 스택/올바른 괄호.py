def solution(s):
    stack = []

    # 닫는 괄호가 먼저 나오면 False
    if s[0] == ')':
        return False
    
    for b in s:
        # 여는 괄호는 스택에 삽입
        if b == '(':
            stack.append(b)
        # 닫는 괄호가 먼저 나오면 False
        elif b == ')' and len(stack) == 0:
            return False
        # 짝이 맞으면 삭제
        elif b == ')' and stack[-1] == '(':
            stack.pop()

    # 짝 없는 괄호가 남으면 False
    if len(stack) > 0:
        return False
    
    return True
