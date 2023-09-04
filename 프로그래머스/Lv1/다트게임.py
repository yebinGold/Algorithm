# 2018 KAKAO BLIND RECRUITMENT 기출문제

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    scores = [0] # 점수판
    s = "" # 맞춘 점수
    
    for x in dartResult:
        if x.isdigit():
            s += x
        elif x in bonus.keys():
            scores.append(int(s) ** bonus[x])
            s = ""
        elif x == '*':
            scores[-1] *= 2; scores[-2] *= 2
        elif x == '#':
            scores[-1] *= -1
        
    return sum(scores)


# 주어진 문자열을 순회하면서 하나씩 해결!
# 이때, 점수로 한 자리 수가 아닌 10이 주어지는 경우를 처리하기 위해 변수 s를 선언하여 문자열 내에 숫자(점수)가 들어오는 경우를 따로 저장했다.
  
# 이렇게 if-elif를 주르륵 나열하는 코드가 과연 좋은 코드일까? 를 고민하면서도 결국 오늘도 if-elif..
