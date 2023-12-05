def solution(array, commands):
    """ commands의 [i, j, k]에 대해서 array를 i번째부터 j번째까지 슬라이싱으로 자르고 정렬한 결과에서 k번째 값을 뽑아낸다. """
    return [sorted(array[i-1:j])[k-1] for [i, j, k] in commands]
