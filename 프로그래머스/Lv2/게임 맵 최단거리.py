def solution(maps):
    n, m = len(maps), len(maps[0])
    q = [(0, 0, 1)] # 시작점
    end = (n-1, m-1) # 상대방 진영
    
    visited = [
        [False] * m
        for _ in range(n)
    ]
    visited[0][0] = True
    
    while q:
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
        
        x, y, cnt = q.pop(0)
        if (x, y) == end:
            return cnt
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (nx >= 0 and nx < n and ny >= 0 and ny < m) and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    
    return -1
        
