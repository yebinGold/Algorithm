def solution(participant, completion):
  participant.sort()
  completion.sort()
    
  for p_name, c_name in zip(participant, completion):
      if p_name != c_name:
          return p_name
    
  return participant[-1]


"""

마라톤 완주 실패한 1인에게 확인사살을 날려버리는.. 슬픈 문제

풀기 전에 해당 문제가 해시 문제로 분류되어 있는 걸 봤는데 그냥 마음대로 풀어버렸다.

일단 c(completion)가 p(participant)의 부분집합이니 배열을 정렬하면 동명이인이건 뭐건 같은 이름이 같은 순서대로 정렬될 것이고,
같은 순서에서 c에는 없고 p에만 있는 이름이 나올 때까지 두 배열 원소를 하나씩 비교해줬다.

만약 c의 길이만큼 돌았는데도 p와 c에 들어있는 원소가 모두 같다면 미완주자는 p 배열 맨 마지막에 있는 1인!

일단 맞기는 맞았는데,, 이 문제를 어떻게 해시로 푼다는 건지 전혀 감도 못 잡겠다. 역시 이론과 응용은 별개의 것

"""


# 해시를 사용한 (다른 사람의) 풀이
def solution(participant, completion):
  answer = ""
  temp = 0
  dict = {}

  for part in participant:
    dict[hash(part)] = part
    temp += int(hash(part))

  for com in completion:
    temp -= hash(com)

  answer = dict[temp]
  
  return answer

"""

해시 함수에 key로 이름을 넣어서 구한 고유 해시 값을 전체 참가자만큼 모두 더하고, 완주자만큼 모두 빼서 남은 한 명을 구한다.

확실히 빠르고 간결한 풀이라는 생각이 들었다.
응용을 잘 하면 이렇게도 짤 수 있구나

"""
