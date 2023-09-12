def solution(ingredient):
    answer = 0
    stack = []
    
    for x in ingredient:
        # push
        stack.append(x);
        
        # pop
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4): 
                stack.pop(-1)
            answer += 1

    return answer


"""

스택 기능을 리스트로 구현해서 사용했다.

첫 코드에서 재료를 삭제할 때 슬라이싱을 사용했는데, 슬라이싱할 때마다 거의 n만큼 돌아서 타임아웃 발생
-> pop 연산을 4번 반복하는 걸로 수정해서 통과했다.


⭐슬라이싱 arr[a, b]의 시간복잡도는 O(b-a)
작은 사이즈를 슬라이싱할 거 아니라면 반복문 내에서 쓰지 말 것

"""
