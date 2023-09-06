def solution(progresses, speeds):
    answer = []
    left = len(progresses) # 배포해야 할 총 기능 수
    day = 1 # 작업 일 수
    release = 0 # 하루에 배포 가능한 기능 수
    
    while left > 0:
        if progresses[0] + (day * speeds[0]) >= 100:
            progresses.pop(0); speeds.pop(0)
            release += 1; left -= 1
        else:
            if release > 0:
                answer.append(release)
            release = 0
            day += 1

    # 마지막 날 배포
    if release > 0:
        answer.append(release)
            
    return answer

"""

이전에 작성했던 중첩 반복문 코드 대신 반복문을 한 번만 사용하는 코드로 수정한 버전
직접 배열의 값을 업데이트하는 것이 아니라 시간을 고려한 계산을 통해 값을 시뮬레이션 해줬다.

"""
