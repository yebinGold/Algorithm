function solution(my_string) {
    const exp = my_string.split(" ");
    let answer = parseInt(exp[0]);
    
    for(let i = 1; i < exp.length; i = i + 2){
        const op = exp[i];
        if(op == '+'){
            answer = answer + parseInt(exp[i+1]);
        } else {
            answer = answer - parseInt(exp[i+1]);
        }
    }
    
    return answer;
}
