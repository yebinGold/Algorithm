def make_checklist(X):
    """ X에 들어있는 정수와 그 개수를 세서 딕셔너리로 저장 """
    checklist = {}
    for x in list(set(X)):
        checklist[x] = X.count(x)
      
    return checklist


def solution(X, Y):
    answer = []
    X = make_checklist(X)
    
    for num in Y:
        if num in X and X[num] != 0:
            answer.append(num)
            X[num] -= 1
    
    # 짝궁이 존재하지 않는 경우
    if len(answer) == 0: return "-1"
      
    # 가장 큰 정수를 구하기 위해서 숫자 내림차순 정렬
    answer.sort(reverse=True)
    # 짝궁이 0으로만 구성되어 있는 경우
    if answer[0] == "0": return "0"
      
    return "".join(answer)
