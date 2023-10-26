# 2020 KAKAO BLIND RECRUITMENT

import sys

def zip(s, n):
    """ 문자열 s를 n개 단위로 잘라 압축한 결과의 길이를 반환하는 함수 """
    split_s = [s[i:i + n] for i in range(0, len(s), n)]  # n개 단위로 문자열을 잘라서 리스트로 저장
    zip_s = ""                                           # 압축 결과를 저장할 문자열
    prev = split_s[0]; idx = 1; repeat = 1               # 이전 문자열(반복 체크 대상), 현재 인덱스, 반복 횟수 
    
    while idx < len(split_s):
        curr = split_s[idx] # 현재 문자열
      
        # 이전에 나온 문자열과 같으면
        if prev == curr:
            repeat += 1  # 반복 +1
          
        # 이전에 나온 문자열과 다르면
        else:
            # prev와 반복 횟수를 문자열에 저장
            if repeat > 1:
                zip_s += str(repeat) + prev
            else:
                zip_s += prev
              
            # 현재 문자열을 반복 체크 대상으로 갱신하고 반복 상태 초기화
            prev = curr
            repeat = 1

        # 다음 문자열로 넘어감
        idx += 1

    # 최종 결과에 마지막 문자열 반복 여부 반영
    if repeat > 1:
        zip_s += str(repeat) + prev
    else:
        zip_s += prev
        
    return len(zip_s)


def solution(s):
    answer = sys.maxsize  # 최솟값 비교를 위해 초깃값을 큰 수로 지정

    # 예외처리, 문자열 길이가 1이라면 어떻게 압축해도 최소 길이는 1
    if len(s) == 1:
        return 1

    # 압축 가능한 단위 => 1개 단위로 문자열 개수만큼 압축 ~ 절반 크기로 나눠 2번 압축 
    for n in range(1, len(s) // 2 + 1):
        answer = min(answer, zip(s, n)) # 문자열 s를 n개 단위로 잘라 압축한 결과
    
    return answer


# 예제 테스트 결과
# 문자열 'ababcdcdababcdcd'를 압축한 결과의 최소 길이

# 출력: <압축 단위  압축 단위로 문자열 분할  최종 압축 결과>
1 ['a', 'b', 'a', 'b', 'c', 'd', 'c', 'd', 'a', 'b', 'a', 'b', 'c', 'd', 'c', 'd'] ababcdcdababcdcd
2 ['ab', 'ab', 'cd', 'cd', 'ab', 'ab', 'cd', 'cd'] 2ab2cd2ab2cd
3 ['aba', 'bcd', 'cda', 'bab', 'cdc', 'd'] ababcdcdababcdcd
4 ['abab', 'cdcd', 'abab', 'cdcd'] ababcdcdababcdcd
5 ['ababc', 'dcdab', 'abcdc', 'd'] ababcdcdababcdcd
6 ['ababcd', 'cdabab', 'cdcd'] ababcdcdababcdcd
7 ['ababcdc', 'dababcd', 'cd'] ababcdcdababcdcd
8 ['ababcdcd', 'ababcdcd'] 2ababcdcd
