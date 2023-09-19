dict = []

def make_dic(word):
    if len(word) >= 5:
        return
    
    for alp in ['A', 'E', 'I', 'O', 'U']:
        word += alp
        dict.append(word)
        make_dic(word)
        word = word[:-1]

def solution(word):
    make_dic("")
    return dict.index(word) + 1

"""

1. 알파벳 ['A', 'E', 'I', 'O', 'U']로 만들 수 있는 모든 단어를 만들어서 저장한다.
  - 재귀함수를 사용해서 가능한 조합을 찾는다.
  - 재귀 종료조건은 만들 수 있는 가장 긴 조합의 길이까지 도달했을 때 
2. 찾으려는 단어의 인덱스 값을 내장함수로 구한 후 반환한다.
  - 이때 인덱스가 아닌 몇번째 단어인지를 구해야 하기 때문에 +1 

"""
