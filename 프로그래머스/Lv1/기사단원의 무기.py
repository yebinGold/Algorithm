def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        divisor = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num == i ** 2: divisor += 1
            elif num % i == 0: divisor += 2
        
        if divisor > limit:
            answer += power 
        else: answer += divisor
        
    return answer


"""

약수의 개수를 구하는 과정에서 타임아웃이 발생해서 for문의 범위를 제곱근까지 축소하는 걸로 해결했다.
이때 num이 제곱수이면 약수의 개수는 (각 약수의 쌍 + 제곱근)까지 해서 홀수, 그 외의 경우라면 짝수!

"""
