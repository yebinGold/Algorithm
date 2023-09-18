# 완전탐색
from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = {}

    for r in range(1, len(numbers) + 1):
        # r --> 순열의 길이
        for p in permutations(numbers, r):
            num = int("".join(list(p)))
            if is_prime(num):
                answer[num] = 1
    
    return len(answer)


"""

1. 주어진 숫자가 소수인지 여부를 판별하는 is_prime 함수 생성
  - 반복문을 돌려가며 1과 자기 자신 이외의 수 중 나누어 떨어지는 약수가 있는지 확인한다.
  - 시간 단축을 위해 반복문의 범위는 sqrt(num)까지로 한정한다.
2. itertools.permutations를 활용하여 1부터 최대 길이까지의 순열을 생성
3. 반환 받은 순열 tuple을 정수화한 후 is_prime에 넣어 함수를 호출한다.
4. 만약 소수가 맞다면 answer에 저장한다.
  - 이때 중복 처리를 위해 answer은 딕셔너리로, num은 키로 설정하여 저장한다.
  - 같은 값이 나온다면 덮어쓰기
5. 최종적으로 answer 딕셔너리에 저장된 item의 수를 카운트하여 정답을 낸다.

"""
