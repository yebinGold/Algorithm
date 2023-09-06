# Greedy

def solution(n, lost, reserve):
  arr = [0] + [2 if (i in reserve and i not in lost) else 1 for i in range(1, n+1)]

  for i in sorted(lost):
      # 잃어버렸지만 여분이 있는 경우
      if i in reserve: continue
        
      # 앞 친구에게 빌리는 경우
      elif i > 1 and arr[i-1] == 2:
          arr[i-1] -= 1
        
      # 뒷 친구에게 빌리는 경우
      elif i < n and arr[i+1] == 2:
          arr[i+1] -= 1
        
      # 못 빌리는 경우
      else: arr[i] -= 1
        
  return n - arr[1:].count(0)


"""

체육복을 빌려줄 수 있는 (여유분 있는) 학생들을 번호 순으로 관리하기 위해 배열 arr을 만들었다.
이때, 인덱스 = 학생 번호가 될 수 있도록 사용하지 않을 0번 인덱스를 추가했으며
체육복을 잃어버린 학생들의 경우는 따로 arr에 반영하지 않고 값을 1로 통일해서 저장했다. (어차피 해당 값은 안 쓸 거라)


체육복을 잃어버린 학생들을 앞 번호부터 탐색하면서, 여분의 체육복이 있는 앞 번호 / 뒷 번호 학생 중 앞 번호 학생에게 우선적으로 체육복을 빌리도록 작성했다.

ex) 학생 a b c d e 중 a와 c는 여벌 옷이 있고 b와 d는 체육복을 도난당한 경우, b가 c에게 옷을 빌리게 되면 d는 a에게 옷이 남더라도 수업을 못 듣게 된다.
그러니 최대 다수의 수업권을 위해 아묻따 순서대로 제일 앞에 보이는 옷을 빌려 입는 걸로.. (greedy)

"""


"""

맨 위에서 arr 배열 선언할 때 간결하게 써보겠답시고 list comprehension으로 작성해봤는데,
저렇게 되면 for문 한 번 돌 때마다 reserve 배열이랑 lost 배열을 한 번씩 탐색하게 되니까 총 i번씩 탐색하게 되는..?

차라리 arr 배열을 1로 초기화 해놓고 for문으로 reserve 원소를 한 번씩만 가져와서 인덱스처럼 사용하는 게 나았을지도..
그래도 이 문제는 n이 작아서 상관 없으려나

"""
