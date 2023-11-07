from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while len(progresses) > 0:
        deploy = 0
        # 가장 먼저 배포될 작업을 끝내기 위해 필요한 작업일수
        day = ceil((100 - progresses[0]) / speeds[0])

        # 작업일수만큼 모든 작업 진도 증가
        for i in range(len(progresses)):
            progresses[i] += (speeds[i] * day)
          
        # 한 번에 배포 가능한 작업 추출
        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                deploy += 1
            else:
                break
                
        answer.append(deploy)
            
    return answer
