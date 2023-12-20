def solution(array, n):
    # 절댓값을 이용하여 타겟 넘버 n과 array 속 숫자들 간의 차잇값을 비교 후, 값이 가장 작은 수를 찾는다.
    abs_array = [(abs(n - num), num) for num in array]
    return sorted(abs_array)[0][1]
