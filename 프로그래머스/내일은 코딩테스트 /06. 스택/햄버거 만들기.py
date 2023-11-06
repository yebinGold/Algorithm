def solution(ingredient):
    answer = 0
    order = []
    
    for i in ingredient:
        order.append(i)
        if len(order) >= 4 and order[-4:] == [1,2,3,1]:
            for _ in range(4):
                order.pop(-1)
            answer += 1
    
    return answer
