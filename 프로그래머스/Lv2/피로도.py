# 완전탐색
from itertools import permutations

def can_go(k, p):
    go = 0
    for start, end in p:
        if start > k:
            break
        elif end > k:
            break
        k -= end
        go += 1
        
    return go


def solution(k, dungeons):
    answer = -1
    dungeons = list(filter(lambda x: x[0] <= k, dungeons))
    
    for r in range(1, len(dungeons) + 1):
        for p in permutations(dungeons, r):
            answer = max(answer, can_go(k, p))
    
    return answer

"""

1. itertools.permutations를 사용해서 가능한 모든 탐험 순서를 구한다.
2. 하나씩 돌면서 해당 순서에서 탐험할 수 있는 최대 던전 수를 구한다.
3. 최댓값 비교를 하며 가장 큰 수를 골라낸다.

"""
