def solution(num, total):
    answer = []
    temp = (total // num) - (num // 2) if num % 2 != 0 else (total // num) - (num // 2) + 1
    for i in range(num):
        answer.append(temp)
        temp += 1
    
    return answer

"""
num개의 연속된 수를 더해서 total을 만들어야 하기 때문에
answer에 들어갈 수는 (total // num)을 포함한 주변 숫자임을 알 수 있다. 

변수 temp = answer 배열의 첫 번째 수
"""
