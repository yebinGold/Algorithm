def solution(priorities, location):
    answer = 0   

    while len(priorities) > 1:
        # 최고 우선순위 업데이트
        max_p = max(priorities)
        p = priorities.pop(0)
        # 목표 프로세스 실행되면 반복문 종료
        if location == 0 and p == max_p:
            break
        # 가장 큰 우선순위이면 실행하고 location 조정
        if p == max_p:
            answer += 1
            location -= 1
        # 아니라면 맨 뒤로 보내고 location 조정
        elif p != max_p:
            priorities.append(p)
            location -= 1
            if location < 0:
                location = len(priorities) - 1
    
    return answer + 1
