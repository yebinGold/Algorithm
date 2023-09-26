def solution(lottos, win_nums):
    grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 당첨개수:등수
    unknown = 0; correct = 0;
    
    for num in lottos:
        if num == 0:
            unknown += 1
        elif num in win_nums:
            correct += 1
    
    return [grade[correct + unknown], grade[correct]]
