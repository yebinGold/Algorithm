def solution(park, routes):
    row, col = len(park), len(park[0]) # park 범위
    
    # 시작 지점 찾기 (x, y)
    for a in range(row):
        b = park[a].find("S")
        if b != -1:
            x, y = a, b
            break

    # 동서남북 direction
    dirs = {'E':0, 'W':1, 'S':2, 'N':3} # op: index
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for route in routes:
        op, n = route.split(" ")
        nx, ny = x, y # 임시 x, y
        
        for _ in range(int(n)):
            nx, ny = nx + dx[dirs[op]], ny + dy[dirs[op]]
        	
            # 이동 가능 범위 밖인지 or 장애물을 마주하는지 검사
            if (nx < 0 or nx >= row or ny < 0 or ny >= col) or park[nx][ny] == "X":
                nx, ny = x, y # 이동 불가하면 원상복구
                break

        x, y = nx, ny # 이동 가능하면 반영
    
    return [x, y]

"""

각 이동 방향 E, W, S, N이 들어올 때 (세로방향 x, 가로방향 y)의 인덱스 변화를 미리 배열로 저장해서 사용한다.

E -> x + 0, y + 1 : (오른쪽으로 1만큼 이동)
W -> x + 0, y + (-1) : (왼쪽으로 1만큼 이동)
S -> x + 1, y + 0 : (아래쪽으로 1만큼 이동)
N -> x + (-1), y + 0 : (위쪽으로 1만큼 이동)

"""
