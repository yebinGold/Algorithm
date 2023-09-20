def solution(my_string, num1, num2):
    s1 = my_string[num1]; s2 = my_string[num2]
    
    return my_string[:num1] + s2 + my_string[num1+1:num2] + s1 + my_string[num2+1:]
