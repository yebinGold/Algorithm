def solution(X, Y):
    num_x = [0] * 10
    num_y = [0] * 10

    # 각 정수가 나타나는 횟수 카운트
    # X와 Y의 자릿수가 각각 다르기 때문에 따로따로 for문 돌려야 함
    for x in X:
        num_x[int(x)] += 1
        
    for y in Y:
        num_y[int(y)] += 1

    partner = []
    for i in range(10):
        for _ in range(min(num_x[i], num_y[i])):
            # 짝지을 수 있는 개수만큼 사용 가능한 숫자 append
            partner.append(str(i))

    # case 1. 짝꿍이 존재하지 않음
    if not len(partner): return "-1"
    
    # 가장 큰 정수를 만들기 위한 내림차순 정렬
    partner.sort(reverse=True)

    # case 2. 짝꿍이 0으로만 구성됨
    if partner[0] == "0": return "0"

    # case3. 그 외 -> 문자열로 반환
    return "".join(partner)

"""

처음에는 주어진 X와 Y를 순회하며 중복되는 원소가 있는지 체크한 후,
해당 원소를 partners 배열에 추가하고 기존 X, Y에서 제거..
를 반복하는 코드를 짰으나 타임아웃 발생

이후 각 자릿수 범위에 맞게 0부터 9까지의 고정된 배열을 생성.
각 배열 원소의 중복 개수를 세고, 이를 이용해서 두 배열의 중복 원소 개수를 비교하는 코드로 수정했다.

이때, 짝지을 수 있는 숫자를 골라내기 위해 정수 k가 X와 Y에서 각각 나타나는 횟수의 최솟값을 활용했다.
ex) 3이 X에서 2번, Y에서 3번 나왔다면 짝궁 만들기에 사용 가능한 3의 개수는 2개

"""
