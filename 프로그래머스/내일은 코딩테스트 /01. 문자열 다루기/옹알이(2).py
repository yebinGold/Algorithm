def solution(babbling):
    answer = 0
    
    for babb in babbling:
        norepeat = True
        for can in ["aya", "ye", "woo", "ma"]:
            if can + can in babb:
                norepeat = False
                break
            babb = babb.replace(can, ".")
        babb = babb.replace(".", "")
        
        if norepeat and len(babb) == 0:
            answer += 1
    
    return answer
