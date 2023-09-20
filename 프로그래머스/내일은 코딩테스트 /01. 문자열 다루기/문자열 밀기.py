def solution(A, B):
    answer = 0
    a = list(A); b = list(B)
    
    while answer < len(A):
        if A == B:
            return answer
        
        A = A[-1] + A[:-1]
        answer += 1
    
    return -1
