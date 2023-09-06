def solution(progresses, speeds):
    answer = []
    left = len(progresses) # 앞으로 배포해야 할 기능 개수
    
    while left > 0:
        release = 0 # 당일 배포 가능한 기능 개수
        
        # 당일 작업량 반영
        for i in range(left):
            progresses[i] += speeds[i]
        
        # 진도율 100% 달성한 기능 배포
        while left > 0 and progresses[0] >= 100:
            progresses.pop(0); speeds.pop(0)
            release += 1; left -= 1
        
        # 당일 배포한 기능 개수 기록
        if release != 0:
            answer.append(release)
    
    return answer

"""

시간 복잡도를 고려하지 않은 너무 정직한 풀이.
n의 개수가 크지 않아서 실행 속도에 문제는 없었지만, 문제에서 주어진 조건을 너무 그대로 구현하려고 하는 것보다는
유연하게 효율적인 풀이를 생각하는 습관을 들여야 할 듯하다.

"""
