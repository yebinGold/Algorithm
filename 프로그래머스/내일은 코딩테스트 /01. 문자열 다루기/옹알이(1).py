def solution(babbling):
    answer = 0
    for babb in babbling:
        for can in ["aya", "ye", "woo", "ma"]:
            babb = babb.replace(can, ".")
        babb = babb.replace(".", "")
        if len(babb) == 0:
            answer += 1
    
    return answer
