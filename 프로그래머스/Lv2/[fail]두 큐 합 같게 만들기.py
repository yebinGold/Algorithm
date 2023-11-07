# 2022 KAKAO TECH INTERNSHIP

# 1st. 타임아웃
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
