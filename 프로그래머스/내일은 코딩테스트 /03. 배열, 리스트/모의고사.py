def solution(answers):
    answer = []
    grade = [0,0,0]
    a1 = [1,2,3,4,5]; a2 = [2,1,2,3,2,4,2,5]; a3 = [3,3,1,1,2,2,4,4,5,5]
    i1, i2, i3 = 0, 0, 0
    
    for i in range(len(answers)):        
        if a1[i1] == answers[i]:
            grade[0] += 1
        if a2[i2] == answers[i]:
            grade[1] += 1
        if a3[i3] == answers[i]:
            grade[2] += 1
        
        i1 = (i1 + 1) % len(a1)
        i2 = (i2 + 1) % len(a2)
        i3 = (i3 + 1) % len(a3)

    for i, x in enumerate(grade):
        if x == max(grade):
            answer.append(i+1)
    
    return answer
