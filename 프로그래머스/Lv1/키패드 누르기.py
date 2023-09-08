# 2020 카카오 인턴십 기출문제
def solution(numbers, hand):
    answer = ""
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    
    # 시작 위치
    lx, ly = keypad['*']
    rx, ry = keypad['#']
    
    for n in numbers:
        x, y = keypad[n] # n의 키패드 위치
        
        if n in [1, 4, 7]:
            answer += "L"
            lx, ly = (x, y)
        elif n in [3, 6, 9]:
            answer += "R"
            rx, ry = (x, y)
        else:
            l_dist = abs(x - lx) + abs(y - ly) # 왼손과 n 사이 거리
            r_dist = abs(x - rx) + abs(y - ry) # 오른손과 n 사이 거리
            
            if (l_dist < r_dist) or (l_dist == r_dist and hand == "left"):
                answer += "L"
                lx, ly = (x, y)
                    
            elif (l_dist > r_dist) or (l_dist == r_dist and hand == "right"):
                answer += "R"
                rx, ry = (x, y)
    
    return answer

"""

어떻게 풀까 고민하는 데 시간이 좀 걸렸지만 어렵지는 않았던 문제!


처음엔 키패드를 2차원 배열로 구현하고 시뮬레이션을 돌려서 이동거리를 구해볼까 했는데,
키패드 숫자가 몇 개 되지도 않고 마지막 줄("*", 0, "#") 예외처리 하기도 뭐해서 그냥 딕셔너리로 위치 인덱스를 고정시켜놓고 사용했다.

각 위치 사이 거리는 시작점과 목적지의 행과 열 인덱스의 차를 각각 구해서
(가로 방향으로 움직여야 할 거리 + 세로 방향으로 움직여야 할 거리)를 더해주는 방식으로 계산했다.

"""
