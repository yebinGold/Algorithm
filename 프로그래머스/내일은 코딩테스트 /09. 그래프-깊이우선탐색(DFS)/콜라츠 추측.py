# 1) 반복문
def solution(num):
    if num == 0:
        return 0
    
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        
        cnt += 1
        if cnt >= 500:
            return -1

    return cnt


# 2) 재귀함수
def solution(num):
    if num == 0:
        return 0

    return dfs(num, 0)


def dfs(num, cnt):
    if num == 1:
        return cnt
    if cnt >= 500:
        return -1
    
    if num % 2 == 0:
        return dfs(num // 2, cnt + 1)
    else:
        return dfs(num * 3 + 1, cnt + 1)
