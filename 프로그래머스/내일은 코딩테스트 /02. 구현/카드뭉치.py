def solution(cards1, cards2, goal):
    i1, i2 = 0, 0
    
    for word in goal:
        if i1 < len(cards1) and cards1[i1] == word:
            i1 += 1
        elif i2 < len(cards2) and cards2[i2] == word:
            i2 += 1
        else:
            return "No"
    
    return "Yes"

"""
1. 사용 가능한 카드의 인덱스를 순서대로 관리한다.
2. 만약 현재 사용 가능한 카드가 목표 단어라면 다음 카드로 넘어간다. (인덱스 +1)
3. 두 개의 카드 뭉치에서 목표 단어가 없다면 "No" 를 반환한다.
4. 목표 단어를 모두 찾을 때까지 반복하고, 무사히 반복문을 통과했다면 "Yes"를 반환한다.
"""
