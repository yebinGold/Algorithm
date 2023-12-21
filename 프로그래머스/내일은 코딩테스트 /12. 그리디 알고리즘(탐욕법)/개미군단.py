def solution(hp):
    answer = 0
    # 공격력이 높은 개미부터 우선적으로 선발
    while hp > 0:
        if hp >= 5:
            hp -= 5
        elif hp >= 3:
            hp -= 3
        else:
            hp -= 1
            
        answer += 1
            
    return answer
