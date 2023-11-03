def solution(skill, skill_trees):
    answer = 0   # 가능한 스킬트리 개수
    i = 0        # 먼저 나와야 할 선행 스킬 순서
    
    for tree in skill_trees:
        for s in tree:
            # 선행 스킬이 아니면 통과
            if s not in skill:
                continue 
            # 선행 스킬이면
            if s == skill[i]:
                i += 1
            # 선행 스킬 중 하나이지만 나와야 할 순서가 틀리면
            elif s in skill and s != skill[i]:
                answer -= 1
                break
        answer += 1
        i = 0
    
    return answer
