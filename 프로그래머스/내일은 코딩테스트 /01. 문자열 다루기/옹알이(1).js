function solution(babbling) {
    let answer = 0;
    
    for(babb of babbling){
        for(word of ["aya", "ye", "woo", "ma"]){
            babb = babb.replace(word, '.');
        }
        babb = babb.replace(/\./g, '');
        if(babb.length == 0){
            answer++;
            console.log(answer);
        }
    }
    
    return answer;
}


/*

for...of 문으로 배열을 순회하며 문자열 치환

자바스크립트의 문자열 replace 메소드는 파이썬과 달리 모든 문자에 대해서 교체(X) 처음 나오는 문자에 대해서만 문자열 교체가 이루어지기 때문에
정규식을 사용해서 모든 문자에 대해서 문자열을 치환하는 작업을 수행해줬다.

*/
