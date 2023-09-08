def solution(keymap, targets):
    answer = []
    dict = {} # keymap에서 각 알파벳을 얻을 수 있는 최소 터치 횟수를 저장할 딕셔너리
    
    for key in keymap:
        for i, x in enumerate(key):
            if x not in dict:
                dict[x] = i + 1
            else:
                dict[x] = min(dict[x], i + 1)
    
    for target in targets:
        cnt = 0 # 자판 누르는 총 횟수
        
        for x in target:
            # x를 누를 수 없다면 (목표 문자열을 작성할 수 없을 때)
            if x not in dict:
                cnt = -1
                break
            
            # x를 누를 수 있으면 저장해놓은 최소 횟수 가져오기 
            cnt += dict[x]
        
        answer.append(cnt)
    
    return answer

"""

각 알파벳을 입력할 때 눌러야 하는 최소 횟수를 미리 저장해놓고 갖다 썼다.
다시 생각해보니 i가 순서 인덱스라서 10열에 else문은 필요 없을 듯

"""
