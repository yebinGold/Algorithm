def solution(d, budget):
    answer = 0
    for price in sorted(d):
        # 예산을 다 쓸 때까지 작은 금액부터 순서대로 처리
        if budget < price:
            break
        budget -= price
        answer += 1
        
    return answer
