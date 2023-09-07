# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    N = len(board) # 격자 크기 (N * N)
    picked = [0]
    answer = 0
    
    for m in moves:
        for i in range(N):
            x = board[i][m-1]
            
            if x != 0:
                board[i][m-1] = 0
                if picked[-1] == x:
                    picked.pop(-1); answer += 2
                else: picked.append(x)
                
                break

    return answer     


"""

크레인으로 뽑은 인형을 담는 picked 배열을 스택처럼 활용한다.

같은 인형이 스택의 top에 있으면 삭제 (폭발)
아니라면 뽑은 인형을 맨 위에 삽입

"""
