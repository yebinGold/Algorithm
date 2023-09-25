def solution(rsp):
    counter = {'2': '0', '0': '5', '5': '2'}
    answer = ''
    for x in rsp:
        answer += counter[x]
    return answer

"""
각 경우에 대해 이기는 수를 저장한 counter 딕셔너리를 활용
"""
