from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    
    if direction == "right":
        num = numbers.pop()
        numbers.appendleft(num)
    else:
        num = numbers.popleft()
        numbers.append(num)
    
    return list(numbers)
