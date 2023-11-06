def solution(arr):
    answer = [arr.pop(0)]
    
    for x in arr:
        prev = answer[-1]
        if x == prev:
            continue
        else:
            answer.append(x)
    
    return answer
