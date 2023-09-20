def solution(my_string):
    my_string = my_string.split(" ")
    answer = int(my_string[0])
    for s in range(1, len(my_string), 2):
        op = my_string[s]; num = int(my_string[s+1]) 
        if op == '+':
            answer += num
        else:
            answer -= num
    
    return answer
