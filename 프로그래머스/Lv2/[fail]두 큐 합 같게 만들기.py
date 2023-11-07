# 2022 KAKAO TECH INTERNSHIP

# 1st. 타임아웃, 정확성 63.3 (11, 12, 15, 19~24, 28, 30)
def solution(queue1, queue2):
    turn = 0
    
    while sum(queue1) != sum(queue2):
        # 더 이상 넘겨줄 값이 없으면 불가한 것으로 간주
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        # 합이 큰 쪽에서 작은 쪽으로 원소를 넘겨줌
        if sum(queue1) > sum(queue2):
            num = queue1.pop(0)
            queue2.append(num)
        else:
            num = queue2.pop(0)
            queue1.append(num)
        turn += 1
    
    return turn


# 2nd. 타임아웃, 정확성 66.7 (11, 12, 15, 19~24, 30)
def solution(queue1, queue2):
    turn = 0
    first_sum1 = [n for n in queue1]
    
    # 만약 두 정수 배열 원소들의 합이 홀수라면 똑같이 값을 나누는 것이 불가함
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    while sum(queue1) != sum(queue2):
        # 더 이상 넘겨줄 값이 없으면 불가한 것으로 간주
        if (len(queue1) == 0 or len(queue2) == 0):
            return -1
        
        # 두 큐 합이 반복되는 경우
        if turn > 1 and queue1 == first_sum1:
            return -1
        
        # 합이 큰 쪽에서 작은 쪽으로 원소를 넘겨줌
        if sum(queue1) > sum(queue2):
            num = queue1.pop(0)
            queue2.append(num)
        else:
            num = queue2.pop(0)
            queue1.append(num)
        turn += 1
    
    return turn

"""
똑같은 값으로 나누는 것이 불가한 경우를 찾아서 조건 추가
무한루프 발생하는 반례 찾아서 테스트케이스 추가
-> [14, 7, 5, 8] [3, 1, 18, 6]
-> 테스트케이스는 통과했지만 여전히 무한루프 발생 가능성 O

=> 추가 반례를 찾아야 함
"""


# 3rd. 타임아웃, 정확성 96.7 (11)
from collections import deque

def solution(queue1, queue2):
    turn = 0
    # 수행시간 단축을 위해 deque 자료구조 활용
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    first_q1 = deque(queue1)
    
    # 수행시간 단축을 위해 정수 연산으로 합계 관리
    sum1 = sum(queue1); sum2 = sum(queue2)
    
    # 만약 두 정수 배열 원소들의 합이 홀수라면 똑같이 값을 나누는 것이 불가함
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while sum1 != sum2:
        # 더 이상 넘겨줄 값이 없으면 불가한 것으로 간주
        if (len(queue1) == 0 or len(queue2) == 0):
            return -1
        
        # 두 큐 합이 반복되는 경우
        if turn > 1 and (queue1 == first_q1):
            return -1
        
        # 합이 큰 쪽에서 작은 쪽으로 원소를 넘겨줌
        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num; sum2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num; sum2 -= num
        turn += 1
    
    return turn

"""
타임아웃의 원인으로 보이는 sum 연산의 반복을 없애고
수행시간 단축을 위해 deque 자료구조 활용.

대부분의 타임아웃 테스트케이스를 통과했지만, 11번만 예외로 남았다.

<두 큐 합이 반복되는 경우> 처리 코드를 삭제했을 때 11번과 28번에서만 타임아웃이 발생하는 걸로 봐서
무한루프가 발생하는 또다른 반례가 아닐까 예상..

예외 처리 보완 필요.
"""
