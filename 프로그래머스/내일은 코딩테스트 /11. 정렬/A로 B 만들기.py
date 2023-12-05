def solution(before, after):
    # before와 after의 구성요소가 모두 같으면 1을 반환, 아니면 0을 반환
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
