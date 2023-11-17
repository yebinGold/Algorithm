from heapq import heapify, heappush, heappop

def solution(n, works):
    # 주어진 시간만큼 일한 후 남은 작업량이 없는 경우
    if sum(works) <= n:
        return 0

    # heapq를 활용한 최대 힙 구현
    works = [-w for w in works]
    heapify(works)

    # 작업량이 가장 많이 남은 작업부터 1씩 처리
    for _ in range(n):
        work = -heappop(works)
        heappush(works, -(work - 1))
    
    return sum([w ** 2 for w in works])
