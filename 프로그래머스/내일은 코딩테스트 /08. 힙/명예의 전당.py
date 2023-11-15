from heapq import heappush, heappop

def solution(k, score):
    answer = []
    honor = []
    
    for s in score:
        if len(honor) < k:
            heappush(honor, s)
        else:
            if honor[0] < s:
                heappop(honor)
                heappush(honor, s)

        # heap[0]은 항상 최솟값
        answer.append(honor[0])

    return answer
