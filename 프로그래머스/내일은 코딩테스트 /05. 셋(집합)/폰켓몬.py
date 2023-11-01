def solution(nums):
    choose = len(nums) // 2  # 고를 수 있는 폰켓몬 수
    type = len(set(nums))    # 고를 수 있는 폰켓몬 타입 개수

    if choose <= type:
        return choose
    
    return type
