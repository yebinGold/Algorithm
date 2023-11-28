"""
BFS 너비우선탐색
- 큐 자료구조를 활용하여 가까운 정점부터 방문하면서 그래프를 탐색하는 알고리즘
- 최소 방문 횟수를 보장하기 때문에 최단 거리, 최소 이동횟수를 구하는 문제에 사용하기 좋다.
"""

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0]) # (n * m) 크기 맵
    q = deque([(0, 0, 1)]) # 현재 위치 (시작점), 지나간 칸의 개수
    end = (n-1, m-1) # 도착점
    
    visited = [[0 for _ in range(m)] for _ in range(n)] # 자리 방문 여부 기록 배열
    visited[0][0] = 1 # 초기 설정
    
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 맵 내 x, y 이동 좌표 (동서남북)
    
    while q:
        x, y, count = q.popleft() # 현재 위치
        if (x, y) == end:
            return count
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy # 다음 위치
            if (nx >= 0 and nx < n and ny >= 0 and ny < m) and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, count + 1))
    
    return -1
