def solution(numbers, target):
    global answer; answer = 0
    
    def add(x, i):
        """x에 i번째 number를 더하는 함수"""
        global answer

        # 주어진 숫자를 다 썼으면 타겟넘버 확인
        if i == len(numbers):
            if x == target:
                answer += 1
            return
        
        add(x + numbers[i], i+1) # 양수
        add(x + numbers[i]*(-1), i+1) # 음수
    
    add(0, 0)
    
    return answer
