from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    # 스코빌 지수가 K를 넘지 않는 경우가 하나라도 있다면 반복
    while any(s < K for s in scoville):
        # 더 이상 2개 스코빌 지수를 합칠 수 없는 경우 또는 모든 지수가 0인 경우
        if len(scoville) <= 1 or all(s == 0 for s in scoville):
            return -1
        
        fir = heappop(scoville); sec = heappop(scoville)
        new = fir + (sec * 2)
        heappush(scoville, new)
        
        answer += 1
        
    return answer
