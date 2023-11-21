# 1차 시도: 런타임 에러 (테스트 1, 2)
from heapq import heappush, heappop

def solution(tickets):
    global flights, answer, done
    flights = {}; answer = []
    done = len(tickets) + 1 # 총 방문 횟수(최초 출발지 + 항공권 개수)
    
    # 출발지: [도착지1, 도착지2, ...]로 정리
    # 힙큐 알고리즘을 이용하여 우선순위(알파벳 순서) 정렬
    for dep, des in tickets:
        if dep in flights:
            heappush(flights[dep], des)
        else:
            flights[dep] = [des]
    
    # 'ICN' 공항에서 출발
    fly("ICN")
    
    return answer

def fly(dep):
    # 출발지 방문
    answer.append(dep)
    # 모든 도시를 방문했으면 끝
    if len(answer) == done:
        return
    # 방문 가능한 도착지 중 우선순위가 높은 도착지
    des = heappop(flights[dep])
    # 도착지를 출발지로 설정하여 다시 반복
    return fly(des)
