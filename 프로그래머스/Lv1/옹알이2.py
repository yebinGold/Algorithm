def solution(babbling):
    answer = 0
    do = ["aya", "ye", "woo", "ma"] # 가능한 발음
    
    for babb in babbling:
        for x in do:
            # 같은 발음이 연속해서 나오는 경우 제외
            if x + x in babb: break
            # 가능한 발음이 포함되는 경우
            if x in babb: babb = babb.replace(x, " ")
        
        # 불가능한 발음이 포함되어 있지 않으면 +1
        babb = babb.replace(" ", "")
        if len(babb) == 0:
            answer += 1
    
    return answer

"""

우선 주어진 문자열 배열에서 같은 발음이 연속해서 나오는 경우를 뺀 나머지 문자열에 대해 불가능한 발음이 포함되어 있는지 여부를 파악했다.
(가능한 발음들을 삭제해가면서 제거 불가능한 찌꺼기.. 가 남는지 판단)

BUT 통과 가능한 발음을 지운 후에 남은 앞뒤 발음들이 합쳐져 통과 가능한 새로운 발음이 생성되는 문제를 발견했다.
ex) womao에서 ma를 제거 -> woo

문제 해결읠 위해 완전삭제 대신 replace 메소드를 사용해서 지워진 자리를 공백으로 관리해줌!

"""
