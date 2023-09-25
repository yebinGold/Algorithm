def solution(i, j, k):
    answer = 0
    k = str(k)
    
    for num in range(i, j+1):
        for n in str(num):
            if n == k:
                answer += 1
    
    return answer
