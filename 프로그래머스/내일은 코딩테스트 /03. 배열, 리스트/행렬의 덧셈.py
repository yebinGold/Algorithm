def solution(arr1, arr2):
    answer = []
    row = len(arr1); col = len(arr1[0])
    
    for a1, a2 in zip(arr1, arr2):
        temp = []
        for i in range(col):
            temp.append(a1[i] + a2[i])
        answer.append(temp)    
    
    return answer
