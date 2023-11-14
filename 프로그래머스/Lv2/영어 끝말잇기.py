def solution(n, words):
    turn = 1 # 차례
    spoken = [words[0]]

    for i, word in enumerate(words[1:], start=1):
        if i % n == 0: turn += 1
        
        prev = spoken[-1]
        if word in spoken or prev[-1] != word[0]:
            return [i % n + 1, turn] # 탈락자 번호, 차례
        
        spoken.append(word)
    
    return [0, 0]

"""
주어진 단어 배열을 돌면서 이미 나온 단어나 끝말잇기가 제대로 되지 않은 단어를 말한 사람을 찾아서 [번호, 현재 차례]를 리턴한다.

현재 인덱스를 사람 수 n으로 나눈 나머지를 구해서 0, 1, 2, ... , n이 반복되도록 한 후 +1을 하여 현재 발화한 사람의 번호를 구한다.
현재 게임 차례는 turn 변수로 관리하며, 1번 사람의 차례가 돌아오면 turn++ 를 해준다.
"""
