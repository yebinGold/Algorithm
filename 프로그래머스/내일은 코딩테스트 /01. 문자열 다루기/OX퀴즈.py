def solution(quiz):
    answer = []
    
    for q in quiz:
        n1, op, n2, _, result = q.split(" ")
    
        if op == '+':
            if int(n1) + int(n2) == int(result):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(n1) - int(n2) == int(result):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer
